from .options import *


class NetworkServer:

    def get_network_servers_list(token: str):
        return make_get('api/network-servers?limit=99999999999', token)


if __name__ == '__main__':
    pass
