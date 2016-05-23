import random

from pyramid_handlers import action

from theapp.controllers.base_controller import BaseController


class ApiController(BaseController):

    @action(renderer='json')
    def active_user_count(self):
        count = random.randint(10000, 20000)
        return {'count': count}

    @action(renderer='json')
    def submit_data(self):
        the_data = self.request.json_body
        print(the_data)
        return the_data