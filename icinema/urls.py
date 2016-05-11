from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView

from models import *
from forms import *
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
    #URL for edit cinemes.
    url(r'^cinemes/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
        CinemaDetail.as_view(),
        name='cinema_detail'),

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

    #Create view for update details of films
    url(r'^cinemes/(?P<pkr>\d+)/films/(?P<pk>\d+)/edit/$', UpdateView.as_view(
       model=Films,
       template_name='icinema/form.html',
       form_class=FilmEditForm),
       name='film_edit'),

    #Necessary for a return correct by edit parameters of films
    url(r'^cinemes/(?P<pk>\d+)/films/(\.(?P<extension>(json|xml)))?$',
       FilmsDetail.as_view(),
       name='films_detail'),

    # Create view for update details of cinema
    url(r'^cinemes/(?P<pk>\d+)/edit/$', UpdateView.as_view(
       model=Cinema,
       template_name='icinema/form.html',
       form_class=CinemaForm),
       name='cinema_edit'),

    # Create Films
    url(r'^cinemes/(?P<pkr>\d+)/films/create$', FilmCreate.as_view(), name='film_create'),

    # Create Performances (Hours, Sala )
    url(r'^cinemes/(?P<pkr>\d+)/films/(?P<pk>\d+)/add_performance$', PerformanceCreate.as_view(), name='performance_create'),

    # Create view for edit details of performances
    url(r'^cinemes/(?P<pkr>\d+)/films/(?P<pk>\d+)/edit_performance/$', UpdateView.as_view(
       model=Performances,
       template_name='icinema/form.html',
       form_class=PerformancesEditForm),
       name='performances_edit'),




)