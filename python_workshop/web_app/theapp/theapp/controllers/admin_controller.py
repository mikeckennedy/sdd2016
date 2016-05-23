from pyramid_handlers import action
import pyramid.httpexceptions

from theapp.controllers.base_controller import BaseController
from theapp.services.post_service import PostService
from theapp.viewmodels.new_post_viewmodel import NewPostViewModel


class AdminController(BaseController):
    @action(renderer='theapp:/templates/admin/index.pt')
    def index(self):
        return {}

    @action(
        name='add_post',
        request_method='GET',
        renderer='theapp:/templates/admin/add_post.pt')
    def add_post_get(self):
        vm = NewPostViewModel()
        return vm.to_dict()

    @action(
        name='add_post',
        request_method='POST',
        renderer='theapp:/templates/admin/add_post.pt')
    def add_post_post(self):
        vm = NewPostViewModel()
        vm.from_dict(self.data)

        if vm.check_for_errors():
            return vm.to_dict()

        PostService.create_post(vm.title, vm.url)

        raise pyramid.httpexceptions.HTTPFound('/')
