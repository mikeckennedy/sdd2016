import pyramid_handlers

from theapp.controllers.base_controller import BaseController
from theapp.services.post_service import PostService


class HomeController(BaseController):

    @pyramid_handlers.action(renderer='theapp:/templates/home/index.pt')
    def index(self):
        try:
            # PostService.create_posts()

            posts = PostService.all_posts()

            return {'posts': posts}
        except Exception as x:
            print("Ooops! {}".format(x))
            return {'posts': []}

    @pyramid_handlers.action(renderer='theapp:/templates/home/about.pt')
    def about(self):
        return {"Hello": "About"}
