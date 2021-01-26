"""Khoojee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path

from app.view.details_page import user_details
from app.view.home_page import home, username_home
from app.view.search_domain_info import home as domain_info
from app.view.search_mobile import mobile_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home_page"),
    path('domain_info/', domain_info, name="domain_info"),
    path('username_info/', username_home, name="username_info"),
    path('mobile_info/', mobile_home, name="mobile_info"),
url('^user_details/$', user_details, name='user_details'),
    re_path('search/', include('app.urls')),
    re_path('ajax/', include('app.ajax.urls')),

]
