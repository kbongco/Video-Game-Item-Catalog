from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Videogames, User, Genre

engine = create_engine('sqlite:///VideoGamesCatalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

#Dummy Video Games Data
#ICDH = Insert Creative Description Here

User1 = User(name ="Chibi", email="whoa.its.chibi@gmail.com")
session.add(User1)
session.commit()

#Create Genres
genre1 = Genre(user_id =1, name="JRPG")
session.add(genre1)
session.commit()

genre2 = Genre(user_id=1, name ="Hero Based Shooter")
session.add(genre2)
session.commit()

genre3=Genre(user_id=1, name="Rhythm")
session.add(genre3)
session.commit()

genre4=Genre(user_id=1, name="Action/Adventure")
session.add(genre4)
session.commit()

genre5=Genre(user_id=1, name="Horror")
session.add(genre5)
session.commit()

genre6=Genre(user_id=1, name="Platformer")
session.add(genre6)
session.commit()

genre7=Genre(user_id=1, name="Battle Royale")
session.add(genre7)
session.commit()

genre8 = Genre(user_id =1, name ="Fighter")
session.add(genre8)
session.commit()

genre9 = Genre(user_id =1, name ="Sports")
session.add(genre9)
session.commit()

genre10 = Genre(user_id = 1, name ="Puzzle")
session.add(genre10)
session.commit()


#Create Game to Genre
VG1=Videogames(gameName = "Overwatch", companyName ="Blizzard Entertainment",
	coverUrl ="#", releaseYear="2016", description ="ICDH", genre = genre2, 
	platform = "PC,Xbox One, Playstation 4")
session.add(VG1)
session.commit()

VG2=Videogames(gameName = "Ryu ga Gotoku (Like a dragon):0", companyName="Sega",
	coverUrl ="#", releaseYear ="2015", description ="ICDH", genre = genre1,
	platform ="Playstation 4")
session.add(VG2)
session.commit()

VG3=Videogames(gameName = "Dance Dance Revolution", companyName="Konami",
	coverUrl ="#", releaseYear="1998", description ="ICDH", genre = genre3,
	platform ="Arcade")
session.add(VG3)
session.commit()

VG4=Videogames(gameName ="Persona 5", companyName="Atlus", coverUrl="#",
	releaseYear="2017", description ="ICDH", genre = genre1, platform="Playstation 4")
session.add(VG4)
session.commit()

VG5=Videogames(gameName="Super Mario Bros", companyName="Nintendo", coverUrl="#",
	releaseYear="1985", description="ICDH", genre=genre6, platform="Nintendo Entertainment System")
session.add(VG5)
session.commit()

VG6=Videogames(gameName="Fortnite", companyName="Epic Games", coverUrl="#",
	releaseYear ="2017", description="ICDH", genre = genre7, 
	platform ="PC, XBOX One, Playstation 4, Mobile, Nintendo Switch")
session.add(VG6)
session.commit()

VG7=Videogames(gameName="The Legend of Zelda: Ocarina of Time", companyName="Nintendo",
	coverUrl="#", releaseYear="1998", description ="ICDH", genre = genre4, platform = "Nintendo 64")
session.add(VG7)
session.commit()

VG8=Videogames(gameName="Five Nights at Freddy's", companyName="Scott Games", 
	coverUrl="#", releaseYear="2014", description="ICDH", genre= genre5, platform ="PC, Mobile")
session.add(VG8)
session.commit()

print('Added everything!')
