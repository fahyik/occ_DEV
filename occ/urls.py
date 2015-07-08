"""occ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from occ_survey.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^survey/', include('occ_survey.urls', namespace="occ_survey")),
    url(r'^$', index, name="index"),
    url(r'^dashboard/(?P<username>[\w\-]+)/$', dashboard, name="dashboard"),
    url(r'^about/$', about, name="about"),
    url(r'^buttons/$', buttons, name="buttons"),
    url(r'^user_login/$', user_login, name="user_login"),
    url(r'^user_logout/$', user_logout, name="user_logout"),
    url(r'^get_status/$', get_status, name="get_status"),
]
