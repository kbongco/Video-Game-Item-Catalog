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

class Platform(Base):
	__tablename__ = "Platform"

	id =Column(Integer,primary_key = True)
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

class VideoGames(Base):
	__tablename__ ='video_games'
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	company = Column(String(80), nullable = False)
	releaseyear = Column(String(80), nullable = False)
	description = Column(String(250), nullable = False)
	platform_id = Column(Integer, ForeignKey('Platform.id'))
	platform = relationship(Platform)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property 
	def serialize(self):
		return {
			'name':self.name,
			'id':self.id,
			'company':self.company,
			'releaseyear':self.releaseyear,
			'description':self.description,
			'platform': self.platform.name,
		}

engine = create_engine('sqlite:///VideoGamesCatalog.db')

Base.metadata.create_all(engine)
