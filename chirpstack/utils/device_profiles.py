from .options import *


class DeviceProfiles:

    def get_device_profiles_list(token: str):
        return make_get('api/device-profiles?limit=99999999999', token)

    def create_new_device_profile(body: dict, token: str) -> dict:
        return make_post('api/device-profiles', body, token)


if __name__ == '__main__':
    pass
