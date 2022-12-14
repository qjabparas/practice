from .paths import PathsApi, PathApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
    api.add_resource(PathsApi, '/api/paths')
    api.add_resource(PathApi, '/api/paths/<id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')