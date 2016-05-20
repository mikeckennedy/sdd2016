import datetime

from theapp.models.sql_base import SqlAlchemyBase
import sqlalchemy
# import uuid


class Post(SqlAlchemyBase):
    __tablename__ = 'Post'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    # id = sqlalchemy.Column(sqlalchemy.String,
    #                        primary_key=True,
    #                        default=lambda : str(uuid.uuid4()).replace('-', ''))

    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    url = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    created = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    # comments = []


# class Comment(SqlAlchemyBase):
#     __tablename__ = 'Comment'
#
#     user = ''
#     created = datetime.datetime.now()
#     post_id = 0
