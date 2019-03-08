from flask import Flask, render_template, request, redirect
from flask import jsonify, url_for, flash, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Platform, VideoGames
import requests
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json

app = Flask(__name__)

engine = create_engine('sqlite:///VideoGamesCatalog.db',
                       connect_args={'check_same_thread': False})

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Video Games Item Catalog"


# GConnect Information
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# Actual Gconnect code
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validating state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain Authorization Code
    code = request.data

    try:
        # Upgrading the authorization code ---> credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Checking the access token if it is valid
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # An error in the access token info will be aborted
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # The access token will be verified for intended user
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
            'Current user is already connected.'),
            200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Storing access token in the session for later use
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Getting user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome,'
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px; border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# Login Credentials
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
        'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(id=user_id).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


# GDISCONNECT CODE

@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # Reset user session
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = redirect(url_for('Platforms'))
        flash("You are now logged out.")
        return response
    else:
        # If the token is invalid
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
    response.headers['Content-Type'] = 'application/json'
    return response


# JSON APIS to view information
@app.route('/platforms/JSON')
def platformsJSON():
    platforms = session.query(Platform).all()
    return jsonify(platforms=[p.serialize for p in platforms])


@app.route('/platforms/<int:platform_id>/games/JSON')
def platformgamesJSON(platform_id):
    platforms = session.query(Platform).filter_by(
        id=platform_id).one()
    games = session.query(VideoGames).filter_by(
        platform_id=platform_id).all()
    return jsonify(VideoGames=[g.serialize for g in games])


# Showing the Platforms for Games
@app.route('/')
@app.route('/platforms')
def Platforms():
    platforms = session.query(Platform).all()
    return render_template('Platforms.html', platforms=platforms)


@app.route('/platforms/new', methods=['GET', 'POST'])
def newplatform():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newplatform = Platform(name=request.form['name'])
        session.add(newplatform)
        session.commit()
        return redirect(url_for('Platforms'))
    else:
        return render_template('newplatform.html')


@app.route('/platforms/<int:platform_id>/edit/', methods=['GET', 'POST'])
def editplatform(platform_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedplatform = session.query(Platform).filter_by(id=platform_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedplatform = request.form['name']
            flash('You changed the name!')
            return redirect(url_for('Platforms'))
    else:
        return render_template('editplatform.html', platform=editedplatform)


@app.route('/platforms/<int:platform_id>/delete', methods=['GET', 'POST'])
def deleteplatform(platform_id):
    if 'username' not in login_session:
        return redirect('/login')
    deleteplatform = session.query(Platform).filter_by(
        id=platform_id).one()
    if request.method == 'POST':
        session.delete(deleteplatform)
        flash('Say bye to the Platform!')
        session.commit()
        return redirect(url_for('Platforms'))
    else:
        return render_template('deleteplatform.html', platform=deleteplatform)


# Viewing Games in the categoriess

@app.route('/platforms/<int:platform_id>/games/')
def games(platform_id):
    platforms = session.query(Platform).filter_by(
        id=platform_id).one()
    games = session.query(VideoGames).filter_by(platform_id=platform_id).all()
    return render_template('viewgames.html',
                           platform_id=platform_id, platforms=platforms,
                           games=games)


@app.route('/platforms/<int:platform_id>/games/new', methods=['GET', 'POST'])
def newgame(platform_id):
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newgame = VideoGames(name=request.form['name'],
                             releaseyear=request.form['releaseyear'],
                             description=request.form['description'],
                             platform_id=platform_id)
        session.add(newgame)
        session.commit()
        flash("New Game was added!")
        return redirect(url_for('games', platform_id=platform_id,
                                newgame=newgame))
    else:
        return render_template('newgame.html', platform_id=platform_id)


@app.route('/platforms/<int:platform_id>/games/<int:game_id>/edit',
           methods=['GET', 'POST'])
def editgame(platform_id, game_id):
    if 'username' not in login_session:
        return redirect('/login')
    editgame = session.query(VideoGames).filter_by(id=game_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editgame.name = request.form['name']
        if request.form['releaseyear']:
            editgame.releaseyear = request.form['releaseyear']
        if request.form['description']:
            editgame.description = request.form['description']
        session.add(editgame)
        session.commit()
        flash('You edited the game!')
        return redirect(url_for('games', platform_id=platform_id))
    else:
        return render_template('editgame.html', platform_id=platform_id,
                               game_id=game_id, g=editgame)


@app.route('/platforms/<int:platform_id>/<int:game_id>/delete',
           methods=['GET', 'POST'])
def deletegame(platform_id, game_id):
    if 'username' not in login_session:
        return redirect('/login')
    deletegame = session.query(VideoGames).filter_by(id=game_id).one()
    if request.method == 'POST':
        session.delete(deletegame)
        session.commit()
        flash('Say bye to the game!')
        return redirect(url_for('games', platform_id=platform_id))
    else:
        return render_template('deletegame.html', platform_id=platform_id,
                               game_id=game_id, g=deletegame)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
