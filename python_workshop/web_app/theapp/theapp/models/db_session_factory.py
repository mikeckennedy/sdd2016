import os
import sqlalchemy
import sqlalchemy.orm
# noinspection PyUnresolvedReferences
import theapp.models.posts

from theapp.models.sql_base import SqlAlchemyBase


class DbSessionFactory:
    factory = None

    @staticmethod
    def create():
        return DbSessionFactory.factory()

    @staticmethod
    def global_init():
        db_file = DbSessionFactory.get_db_file()
        conn_str = 'sqlite:///' + db_file
        engine = sqlalchemy.create_engine(conn_str, echo=False)
        SqlAlchemyBase.metadata.create_all(engine)
        DbSessionFactory.factory = sqlalchemy.orm.sessionmaker(bind=engine)

    @staticmethod
    def get_db_file():
        folder = os.path.dirname(__file__)
        db_file = os.path.join(folder, '..', 'db', 'core.sqlite')
        db_file = os.path.abspath(db_file)
        return db_file
