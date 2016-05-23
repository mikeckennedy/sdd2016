from theapp.models.db_session_factory import DbSessionFactory
from theapp.models.posts import Post


class PostService:
    @staticmethod
    def all_posts():
        session = DbSessionFactory.create()
        posts = session.query(Post).\
            order_by(Post.created.desc()).\
            all()

        session.close()

        return posts

    # @staticmethod
    # def all_posts_millions():
    #     session = DbSessionFactory.create()
    #     posts = session.query(Post).\
    #         order_by(Post.created.desc()).\
    #
    #     for p in posts:
    #         yield p
    #
    #     session.close()


    @classmethod
    def create_posts(cls):
        all_posts = []

        p = Post()
        p.title = 'First post'
        p.url = '/posts/details/first'
        all_posts.append(p)

        p = Post()
        p.title = 'second post'
        p.url = '/posts/details/second'
        all_posts.append(p)

        p = Post()
        p.title = 'Third post'
        p.url = '/posts/details/third'
        all_posts.append(p)

        session = DbSessionFactory.create()
        for p in all_posts:
            session.add(p)

        session.commit()

    @classmethod
    def find_post_by_url(cls, url):
        session = DbSessionFactory.create()

        post = session.query(Post).filter(Post.url == url).first()

        return  post

    @classmethod
    def create_post(cls, title, url):
        session = DbSessionFactory.create()

        p = Post()
        p.title = title
        p.url = url
        session.add(p)

        session.commit()
