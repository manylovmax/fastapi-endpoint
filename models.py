# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///blog.db', echo = True)
# # conn = engine.connect()
# from sqlalchemy import MetaData
# meta = MetaData()

# from sqlalchemy import Table, Column, Integer, String, MetaData
# meta = MetaData()

# students = Table(
#    'students', meta, 
#    Column('id', Integer, primary_key = True), 
#    Column('name', String), 
#    Column('lastname', String), 
# )

# meta.create_all(engine)

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .database import Base


class Post(Base):
   __tablename__ = "posts"

   id = Column(Integer, primary_key=True)
   title = Column(String)
   text = Column(Text)
   

