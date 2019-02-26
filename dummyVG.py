#User, Platform, VideoGame
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Platform, VideoGames

engine = create_engine('sqlite:///VideoGamesCatalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

#Dummy Video Games Data


User1 = User(name ="Chibi", email="whoa.its.chibi@gmail.com")
session.add(User1)
session.commit()

#Create Platform PC and Games
platform1 = Platform(name ="PC", user_id="1")
session.add(platform1)
session.commit()

VideoGame1 = VideoGames(name="Overwatch", 
	description = "You control several heroes shooting objectives!",
	company = "Blizzard Entertainment", releaseyear = '2016',
	platform = platform1, user_id = 1)

session.add(VideoGame1)
session.commit()

VideoGame2 = VideoGames(name="League of Legends", 
	description = "similar to DoTA", company = "Riot Games",
	releaseyear = "2009", platform = platform1, user_id =1)

session.add(VideoGame2)
session.commit()

VideoGame3 = VideoGames(name = "Five Nights at Freddy's",
	description ="5 nights, will you survive?", company = "Scott Games", 
	releaseyear = '2014', platform = platform1, 
	user_id = 1)

session.add(VideoGame3)
session.commit()

#Create Platform PS4 and Games
platform2 = Platform(name = "Playstation")
session.add(platform2)
session.commit()

VideoGame1 = VideoGames(name = "Kingdom Hearts 2.8", 
	description = "Final Chapter before KH3!", company = "Square Enix", 
	releaseyear = "2017", platform = platform2)

session.add(VideoGame1)
session.commit()

VideoGame2 = VideoGames(name = "Ryu Ga Gotoku: 0", 
	description = "Japan 1988.", company = "Sega", 
	releaseyear = "2017",  platform = platform2)
session.add(VideoGame2)
session.commit()

VideoGame3 = VideoGames(name = "Final Fantasy XV", 
	description = "The Fifteenth main installment!", company = "Square Enix",
	releaseyear = "2016", platform = platform2)
session.add(VideoGame3)
session.commit()

#Create Platform Xbox and Games
platform3 = Platform(name = "XBOX")
session.add(platform3)
session.commit()

VideoGame1 = VideoGames(name ="Halo:Combat Evolved", 
	description = "An interstellar war between Humans and the Covenant", 
	company = "Microsoft", releaseyear = "2001",  
	platform = platform3)
session.add(VideoGame1)
session.commit()

VideoGame2 = VideoGames(name = "Fable", description = 
	"ICDH", company = "Microsoft", releaseyear = "2004", 
	platform = platform3)
session.add(VideoGame2)
session.commit()

#Create Platform Nintendo and Games
platform4 = Platform(name = "Nintendo")
session.add(platform4)
session.commit()

VideoGame1 = VideoGames(name = "Super Mario Bros", 
	description = "The Original", company = "Nintendo", releaseyear = "1985",
	platform = platform4)
session.add(VideoGame1)
session.commit()

VideoGame2 = VideoGames(name = "Super Smash Bros: Melee", 
	description = "Nintendo's all stars are back!", company = "Nintendo",
	releaseyear = "2003", platform = platform4)
session.add(VideoGame2)
session.commit()

VideoGame3 = VideoGames(name = "Mario Party", description ="A party game that destroys friendships!",
	company ="Nintendo", releaseyear = "1998", platform = platform4)

print("Games and Platforms Added!")
