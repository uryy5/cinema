from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView

#from models import Films
#from forms import CinemaForm
from views import *

urlpatterns = patterns('',
    # Home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('icinema:cinema_list', kwargs={'extension': 'html'})),
        name='home_page'),

    # List cinemes: /icinema/cinemes.json or html or xml
    url(r'^cinemes\.(?P<extension>(json|xml|html))$',
        CinemaList.as_view(),
        name='cinema_list'),
    # Cinemes films detail
    url(r'^cinemes/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        CinemaDetail.as_view(),
        name='cinema_detail'),
    # Cinemes films list
    url(r'^cinemes/(?P<pk>\d+)/films\.(?P<extension>(json|xml))$',
       FilmsList.as_view(),
       name='films_list'),

    # Cinemes films details
    url(r'^cinemes/(?P<pkr>\d+)/films/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
       FilmsDetail.as_view(),
       name='films_detail'),
    #Cinemes performances list
    url(r'^cinemes/(?P<pk>\d+)/performances\.(?P<extension>(json|xml))$',
       PerformancesList.as_view(),
       name='performances_list'),

   # Cinemes performances details
    url(r'^cinemes/(?P<pkr>\d+)/performances/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
       PerformancesDetail.as_view(),
       name='performances_detail'),
    #Create Cinemes
    url(r'^cinemes/create/$',CinemaCreate.as_view(),name='cinema_create'),
    #Update Cinemes
    url(r'^cinemes/(?P<pk>\d+)/edit/$',UpdateView.as_view(
                               model=Cinema,
                               template_name='icinema/form.html',
                               form_class=CinemaForm),
                               name='cinema_edit'),

)