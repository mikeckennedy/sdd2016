from pyramid.config import Configurator
import theapp.controllers.home_controller as home
import os

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
    config.add_route('home', '/')
    config.add_route('rest', '/rest')

    config.add_handler('home_ctrl_bare', '/home/{action}', handler=home.HomeController)
    config.add_handler('home_ctrl', '/home/{action}/{id}', handler=home.HomeController)

    config.scan()
    return config.make_wsgi_app()
