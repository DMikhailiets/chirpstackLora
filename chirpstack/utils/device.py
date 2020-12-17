from .options import *


class Device:

    def get_devices_list(token: str):
        return make_get('api/devices?limit=99999999999', token)

    def create_new_device(body: dict, token: str) -> dict:
        return make_post('api/devices', body, token)


if __name__ == '__main__':
    pass
