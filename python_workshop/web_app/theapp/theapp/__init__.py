from pyramid.config import Configurator
import theapp.controllers.home_controller as home
import theapp.controllers.posts_controller as posts
import theapp.controllers.admin_controller as admin
import theapp.controllers.api_controller as api
import os

from theapp.models.db_session_factory import DbSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    file = config.get_settings().get('db_file')
    file = os.path.abspath(file)
    print(file)

    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('rest', '/rest')

    config.add_handler('root', '/', handler=home.HomeController, action='index')
    config.add_handler('home_ctrl_bare', '/home/{action}', handler=home.HomeController)
    config.add_handler('home_ctrl', '/home/{action}/{id}', handler=home.HomeController)

    config.add_handler('posts_ctrl', '/posts/{action}/{id}', handler=posts.PostsController)

    config.add_handler('admin_ctrl_root', '/admin', handler=admin.AdminController, action='index')
    config.add_handler('admin_ctrl_root/', '/admin/', handler=admin.AdminController, action='index')
    config.add_handler('admin_ctrl', '/admin/{action}', handler=admin.AdminController)

    config.add_handler('api_ctrl', '/api/{action}', handler=api.ApiController)

    config.scan()

    DbSessionFactory.global_init()

    return config.make_wsgi_app()
