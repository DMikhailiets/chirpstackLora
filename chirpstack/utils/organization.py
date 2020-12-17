from .options import *


class Organization :

    def get_organization_list(token: str) -> dict :
        return make_get(f'api/organizations?limit=99999999999', token)

    def get_organizations_list(token: str, org_id: int) -> dict :
        return make_get(f'api/organizations/{org_id}?limit=9999999', token)

    def create_new_organization(body: dict, token: str) -> dict :
        return make_post('api/organizations', body, token)

    def get_organization_user_list(organization_id: str, token: str) -> dict :
        return make_get(f'api/organizations/{organization_id}/users?limit=9999999', token)

    def add_new_user_to_organization(body, token: str) -> dict :
        return make_post(f'api/users', body, token)


if __name__ == '__main__' :
    pass
