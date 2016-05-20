from pyramid.view import view_config


@view_config(
    route_name='home',
    renderer='templates/mytemplate.pt')
def my_view(request):
    print("Running home...")
    return {'project': 'The project from SDD'}

@view_config(
    route_name='rest',
    renderer='json')
def my_rest(request):
    return {'project': 'The project from SDD', 'day': 'Friday'}
