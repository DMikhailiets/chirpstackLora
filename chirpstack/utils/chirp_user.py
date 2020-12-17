from .options import *


class ChirpUser:

    def get_user_list(token:str) -> dict:
        return make_get('api/users?limit=999999', token)

    def create_new_user(body:dict, token:str) -> dict:
        return make_post('api/organizations', body, token)
    
    def login_user(body:dict, token:str) -> dict:
        return make_post('api/internal/login', body, token)


if __name__  == '__main__':
    pass
