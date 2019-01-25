import sys 

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	email = Column(String(250), nullable = False)
	picture = Column(String(250))

class VideoGamesDB(Base):
	__tablename__ ='VideoGames'

	id = Column(Integer,primary_key = True)
	gameName = Column(String(250), nullable = False)
	companyName = Column(String(250), nullable = False)
	coverUrl = Column(String(250), nullable = False)
	releaseYear = Column(String(250), nullable = False)
	description = Column(String(), nullable = False)
	genre = Column(String(250), nullable = False)
	platform = Column(String(250), nullable = False)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

@property 
def serialize(self):
	return {
	'id': self.id,
	'name': self.gameName,
	'company': self.companyName,
	'year': self.releaseYear,
	'genre': self.genre,
	'coverUrl': self.coverUrl,
	'description': self.description,
	'platform': self.platform
	}


engine = create_engine('sqlite:///VideoGamesCatalog.db')


Base.metadata.create_all(engine)