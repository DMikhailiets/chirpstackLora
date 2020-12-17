from .options import *


class Application:

    def get_applications_list(token: str):
        return make_get('api/applications?limit=99999999999', token)

    def create_new_application(body: dict, token: str) -> dict:
        return make_post('api/applications', body, token)


if __name__ == '__main__':
    pass
