from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa

base = declarative_base()
engine = sa.create_engine('sqlite:///site.db')
base.metadata.bind = engine
session = orm.scoped_session(orm.sessionmaker())(bind=engine)

class Blog(base):
    __tablename__ = 'blog' #<- must declare name for db table
    id = sa.Column(sa.Integer, primary_key=True)
    link = sa.Column(sa.String, nullable=False)
    title = sa.Column(sa.String(255), nullable=False)
    summary = sa.Column(sa.String, nullable=False)
    image = sa.Column(sa.String, nullable=False)
    picture_fn = sa.Column(sa.String(250), nullable=False)
    article_content = sa.Column(sa.String, nullable=False)
