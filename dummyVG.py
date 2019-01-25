from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, VideoGamesDB, User

engine = create_engine('sqlite:///VideoGamesCatalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

#Dummy Video Games Data
#ICDH = Insert Creative Description Here 
VG1 = VideoGamesDB(gameName="Overwatch",
companyName="Blizzard Entertainment",
coverUrl="https://upload.wikimedia.org/wikipedia/en/5/51/Overwatch_cover_art.jpg", 
releaseYear="2016", description ="ICDH", genre="Hero Based Shooter",
platform="PC,XBOX,PS4", user_id = 1)

session.add(VG1)
session.commit()

VG2 = VideoGamesDB(gameName ="Ryu Ga Gotoku:0",
companyName ="Sega", coverUrl ="https://upload.wikimedia.org/wikipedia/en/b/ba/Yakuza0.jpg",
releaseYear ="2015", description ="ICDH", 
genre= "JRPG", platform ="PS4", user_id =1)

session.add(VG2)
session.commit()

VG3 = VideoGamesDB(gameName = "Dance Dance Revolution",
companyName ="Konami", coverUrl ="#", 
releaseYear ="1998", description = "ICDH", genre = "rhythm",
platform = "arcade", user_id =1)

session.add(VG3)
session.commit()

VG4 = VideoGamesDB(gameName = "The Legend of Zelda: Ocarina of Time",
	companyName ="Nintendo", coverUrl = "#",
	releaseYear ="1998", description = "ICDH", genre ="Action/Adventure",
	platform = "N64", user_id = 1)

session.add(VG4)
session.commit()

VG5 = VideoGamesDB(gameName ="Persona 5", companyName ="Atlus",
	coverUrl ="#", releaseYear = "2017", description = "ICDH", 
	genre ="JRPG", platform = "PS4", user_id =1)

session.add(VG5)
session.commit()

VG6 = VideoGamesDB(gameName ="Kingdom Hearts",
	companyName ="Sqaure Enix", coverUrl ="#",
	releaseYear ="2003", description = "ICDH",
	genre ="JRPG", platform = "PS2", user_id = 1)

session.add(VG6)
session.commit()

VG7 = VideoGamesDB(gameName ="Five Nights at Freddy's",
	companyName="Scott Cawthon", coverUrl="#",
	releaseYear ="2014", description ="ICDH",
	genre ="Horror", platform ="PC, Mobile", user_id =1)

session.add(VG7)
session.commit()

VG8 = VideoGamesDB(gameName = "Super Mario Bros",
	companyName="Nintendo", coverUrl="#",
	releaseYear="1985", description="ICDH",
	genre ="platformer", platform ="NES", user_id =1)

session.add(VG8)
session.commit()

print('Added Video Games!')	

