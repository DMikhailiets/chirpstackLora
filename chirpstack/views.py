import json

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from .utils.application import Application
from .utils.chirp_user import ChirpUser
from .utils.device import Device
from .utils.device_profiles import DeviceProfiles
from .utils.network_server import NetworkServer
from .utils.organization import Organization
from .utils.service_profile import ServiceProfile


def process_response(response):
    res = json.loads(JsonResponse(response).content.decode('utf-8'))
    if 'error' in res:
        return Response({'error': res['error']}, status=400)
    else:
        return Response(res)


def redirect_to_frontend(request):
    return redirect('index_page_url', permanent=True)



class Index(View):
    def get(self, request):
        return render(request, 'chirpstack/index.html')


class OrganizationView(APIView):
    def get(self, request):
        """ Отображает список организаций """
        token = request.headers['Token']
        return process_response(Organization.get_organization_list(token))

    def post(self, request):
        """ Создает новую организацию """
        token = request.headers['Token']
        response = json.loads(request.read())
        return process_response(Organization.create_new_organization(response, token))


class OrgranizationUserListView(APIView):
    def get(self, request, org_id=None):
        """ Отображаем всех пользователей конкретной организации """
        token = request.headers['Token']
        return process_response(Organization.get_organization_user_list(org_id, token))


class UserView(APIView):
    def get(self, request):
        """ Отображаем список пользователей """
        token = request.headers['Token']
        return process_response(ChirpUser.get_user_list(token))

    def post(self, request):
        """ Создаем нового пользователя """
        token = request.headers['Token']
        request = json.loads(request.read())
        return process_response(ChirpUser.create_new_user(request, token))


class UserLoginView(APIView):
    def post(self, request):
        token = request.headers['Token']
        request = json.loads(request.read())
        return process_response(ChirpUser.login_user(request, token))


class AddUserToOrgView(APIView):
    def post(self, request):
        """ Добавляет нового пользователя в организацию """
        token = request.headers['Token']
        request = json.loads(request.read())
        return process_response(Organization.add_new_user_to_organization(request, token))


class DevicesView(APIView):
    def get(self, request):
        """ Отображает список базовых станций """
        token = request.headers['Token']
        return process_response(Device.get_devices_list(token))

    def post(self, request):
        """ Создает новую базовую станцию """
        token = request.headers['Token']
        request = json.loads(request.read())
        return process_response(Device.create_new_device(request, token))


class ServiceProfileView(APIView):
    def get(self, request):
        """ Отображает список Service profiles """
        token = request.headers['Token']
        return process_response(ServiceProfile.get_services_profiles_list(token))

    def post(self, request):
        """ Создает новый Service profile """
        token = request.headers['Token']
        request = json.loads(request.read())
        return process_response(ServiceProfile.create_new_service_profile(request, token))


class NetworkServerView(APIView):
    def get(self, request):
        """ Отображает список Network Servers """
        token = request.headers['Token']
        return process_response(NetworkServer.get_network_servers_list(token))


class ApplicationView(APIView):
    def get(self, request):
        """ Отображает список  приложений """
        token = request.headers['Token']
        return process_response(Application.get_applications_list(token))

    def post(self, request):
        """ Создает новый Service profile """
        token = request.headers['Token']
        request = json.loads(request.read())
        return process_response(Application.create_new_application(request, token))


class DeviceProfilesView(APIView):
    def get(self, request):
        """ Отображает список  device profiles """
        token = request.headers['Token']
        return process_response(DeviceProfiles.get_device_profiles_list(token))

    def post(self, request):
        """ Создает новый device profile """
        token = request.headers['Token']
        request = json.loads(request.read())
        return process_response(DeviceProfiles.create_new_device_profile(request, token))
