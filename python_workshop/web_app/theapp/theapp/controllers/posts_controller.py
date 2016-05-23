from pyramid_handlers import action

from theapp.controllers.base_controller import BaseController
from theapp.services.post_service import PostService


class PostsController(BaseController):

    @action(renderer='theapp:/templates/posts/details.pt')
    def details(self):
        url = "/posts/details/" + self.data.get('id')
        post = PostService.find_post_by_url(url)
        if not post:
            pass
            # 404

        return {'title': post.title, 'created': post.created}