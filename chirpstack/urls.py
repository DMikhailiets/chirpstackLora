"""chirpstack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index_page_url'),  # Index Page
    path('api/chirpOrganization', OrganizationView.as_view()),   # get, post
    path('api/listUsersOrg/', OrgranizationUserListView.as_view()),
    path('api/listUsersOrg/<str:org_id>', OrgranizationUserListView.as_view()),  # get
    path('api/user', UserView.as_view()),  # get, post
    path('api/addUserToOrg', AddUserToOrgView.as_view()),  # post
    path('api/chirpLogin', UserLoginView.as_view()),  # post
    path('api/devices', DevicesView.as_view()),  # get, post
    path('api/serviceProfiles', ServiceProfileView.as_view()),  # get, post
    path('api/networkServers', NetworkServerView.as_view()),  # get
    path('api/applications', ApplicationView.as_view()),  # get, post
    path('api/deviceProfiles', DeviceProfilesView.as_view()),  # get, post
    path('home/organizations', redirect_to_frontend),
    path('home/applications', redirect_to_frontend),
    path('home/serviceProfiles', redirect_to_frontend),
    path('home/deviceProfiles', redirect_to_frontend),
    path('home/devices', redirect_to_frontend),
    path('home/orders', redirect_to_frontend),

]
