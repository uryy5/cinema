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

from icinema.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sobres.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^user/(\w+)/$', userpage),
    url(r'^$', mainpage, name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login',name='login'),
    url(r'^icinema/', include('icinema.urls', namespace='icinema')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
    url(r'^admin/', include(admin.site.urls)),
)
