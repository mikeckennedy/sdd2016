import pyramid_handlers
import pyramid.response


class HomeController:
    def __init__(self, request):
        self.request = request

    @pyramid_handlers.action(renderer='theapp:/templates/home/index.pt')
    def index(self):
        return {"Hello": "Index"}

    @pyramid_handlers.action(renderer='theapp:/templates/home/about.pt')
    def about(self):
        return {"Hello": "About"}
