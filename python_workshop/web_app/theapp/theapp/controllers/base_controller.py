from pyramid.renderers import get_renderer


class BaseController:
    def __init__(self, request):
        self.request = request

        layout_renderer = get_renderer(
            'theapp:templates/shared/_layout.pt')

        impl = layout_renderer.implementation()
        self.layout = impl.macros['layout']

        self.data = {}
        self.data.update(self.request.GET)
        self.data.update(self.request.matchdict)
        self.data.update(self.request.POST)
