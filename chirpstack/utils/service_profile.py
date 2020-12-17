from .options import *


class ServiceProfile:

    def get_services_profiles_list(token: str):
        return make_get('api/service-profiles?limit=99999999999', token)

    def create_new_service_profile(body: dict, token: str) -> dict:
        return make_post('api/service-profiles', body, token)


if __name__ == '__main__':
    pass
