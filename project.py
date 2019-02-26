from flask import Flask, render_template, request, redirect , jsonify, url_for, flash
from sqlalchemy import create_engine, asc
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

engine = create_engine('sqlite:///VideoGamesCatalog.db?, check_same_thread = False')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

CLIENT_ID = json.loads(
	open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME ="Video Games Item Catalog"

#Showing the Platforms for Games
@app.route('/')
@app.route('/platforms')
def showPlatforms():
	platforms = session.query(Platform).all()
	return render_template('Platform.html', platforms = platforms)

@app.route('/platforms/new', methods =['GET','POST'])
def newPlatforms():
	if request.method == 'POST':
		newPlatform = Platform(name = request.form['name'])
		session.add(newPlatform)
		session.commit()
		return redirect(url_for('showPlatforms'))
	else:
		return render_template('newPlatform.html')

@app.route('/platforms/<int:platform_id>/edit')
def editPlatform(platform_id):
	editedplatforms = session.query(Platform).filter_by(
		id = platform_id).one()
	if request.method == 'POST':
		if request.form['name']:
			editedplatforms.name = request.form['name']
			flash('You changed the platform!')
			return redirect(url_for('showPlatforms'))
	else:
		return render_template('editPlatform.html', platform = editedPlatform)

@app.route('/platforms/<int:platform_id>/delete', methods = ['GET', 'POST'])
def deletePlatform(platform_id):
	deleteaplatform = session.query(Platform).filter_by(
		id = platform_id).one()
	if request.method == 'POST':
		session.delete(deleteaplatform)
		flash('Say bye to the Platform!')
		session.commit()
		return redirect(url_for('showPlatforms'))
	else:
		return render_template('deletePlatform.html', platform = deleteaplatform)


@app.route('/platforms/<int:platform_id>/games')
def PlatformGames(platform_id):
	platforms = session.query(Platform).filter_by(
		id = platform_id).one()
	games = session.query(VideoGames).filter_by(platform_id = platform_id).all()
	return render_template('VideoGames.html', platforms = platforms, games = games)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)	
