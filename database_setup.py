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
	
class Genre(Base):
	__tablename__ = 'genre'
	id =Column(Integer, primary_key = True)
	name = Column(String(50), nullable = False)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)
	
	@property
	def serialize(self):
		return {
		'id':self.id,
		'name':self.name,
		'user_id':self.user_id
		}

class Videogames(Base):
	__tablename__ ='VideoGames'


	id = Column(Integer,primary_key = True)
	gameName = Column(String(250), nullable = False)
	companyName = Column(String(250), nullable = False)
	coverUrl = Column(String(250), nullable = False)
	releaseYear = Column(String(250), nullable = False)
	description = Column(String(), nullable = False)
	genre_id = Column(Integer, ForeignKey('genre.id'))
	genre = relationship(Genre)
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
	'genre_id':self.genre_id
	'coverUrl': self.coverUrl,
	'description': self.description,
	'platform': self.platform
	'user_id':self.user_id
	}


engine = create_engine('sqlite:///VideoGamesCatalog.db')

Base.metadata.create_all(engine)
