from theapp.viewmodels.base_viewmodel import ViewModelBase


class NewPostViewModel(ViewModelBase):
    def __init__(self):
        self.title = None
        self.url = None
        self.content = None
        self.error = None

    def from_dict(self, d):
        self.title = d.get('title')
        self.url = d.get('url')
        self.content = d.get('content')

    def check_for_errors(self):
        if not self.title or not self.title.strip():
            self.error = "You must specify a title"
        if not self.url or not self.url.strip():
            self.error = "You must specify a url"

        return self.error is not None
