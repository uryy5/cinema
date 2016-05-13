"""cinema URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from rest_framework.urlpatterns import format_suffix_patterns
from views import APIFilmDetail, APIFilmList, APICinemaDetail, APICinemaList, APIPerformancesDetail, APIPerformancesList

urlpatterns = [

    #RESTful API
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/cinema/$', APICinemaList.as_view(), name='cinema-list'),
    url(r'^api/cinema/(?P<pk>\d+)/$', APICinemaDetail.as_view(), name='cinema-detail'),
    url(r'^api/films/$', login_required(APIFilmList.as_view()), name='film-list'),
    url(r'^api/films/(?P<pk>\d+)/$', APIFilmDetail.as_view(), name='film-detail'),
    url(r'^api/performances/$', APIPerformancesList.as_view(), name='performances-list'),
    url(r'^api/performances/(?P<pk>\d+)/$', APIPerformancesDetail.as_view(), name='performances-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'xml'])