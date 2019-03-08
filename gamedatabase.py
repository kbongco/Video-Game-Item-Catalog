# User, Platform, VideoGame
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Platform, VideoGames

engine = create_engine('sqlite:///VideoGamesCatalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Dummy Video Games Data

User1 = User(name="Chibi", email="whoa.its.chibi@gmail.com")
session.add(User1)
session.commit()

# Create Platform PC and Games
platform1 = Platform(name="PC")
session.add(platform1)
session.commit()

VideoGame1 = VideoGames(name="Overwatch",
                        description="Hero Based Shooter!",
                        releaseyear='2016',
                        platform=platform1)

session.add(VideoGame1)
session.commit()

VideoGame2 = VideoGames(name="League of Legends",
                        description="similar to DoTA",
                        releaseyear="2009", platform=platform1)

session.add(VideoGame2)
session.commit()

VideoGame3 = VideoGames(name="Five Nights at Freddy's",
                        description="5 nights, will you survive?",
                        releaseyear='2014', platform=platform1)

session.add(VideoGame3)
session.commit()

# Create Platform PS4 and Games
platform2 = Platform(name="Playstation")
session.add(platform2)
session.commit()

VideoGame1 = VideoGames(name="Kingdom Hearts 2.8",
                        description="Final Chapter before KH3!",
                        releaseyear="2017", platform=platform2)

session.add(VideoGame1)
session.commit()

VideoGame2 = VideoGames(name="Ryu Ga Gotoku: 0",
                        description="Japan 1988.",
                        releaseyear="2017", platform=platform2)
session.add(VideoGame2)
session.commit()

VideoGame3 = VideoGames(name="Final Fantasy XV",
                        description="The Fifteenth main installment!",
                        releaseyear="2016", platform=platform2)
session.add(VideoGame3)
session.commit()

# Create Platform Xbox and Games
platform3 = Platform(name="XBOX")
session.add(platform3)
session.commit()

VideoGame1 = VideoGames(name="Halo:Combat Evolved",
                        description="A war between Humans and the Covenant",
                        releaseyear="2001",
                        platform=platform3)
session.add(VideoGame1)
session.commit()

VideoGame2 = VideoGames(name="Fable",
                        description="Choose your path",
                        releaseyear="2004",
                        platform=platform3)
session.add(VideoGame2)
session.commit()

# Create Platform Nintendo and Games
platform4 = Platform(name="Nintendo")
session.add(platform4)
session.commit()

VideoGame1 = VideoGames(name="Super Mario Bros",
                        description="The Original", releaseyear="1985",
                        platform=platform4)
session.add(VideoGame1)
session.commit()

VideoGame2 = VideoGames(name="Super Smash Bros: Melee",
                        description="Nintendo's all stars are back!",
                        releaseyear="2003", platform=platform4)
session.add(VideoGame2)
session.commit()

VideoGame3 = VideoGames(name="Mario Party",
                        description="Destroys Friendships!",
                        releaseyear="1998", platform=platform4)

print("Games and Platforms Added!")
