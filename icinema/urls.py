from django.conf.urls import patterns, url,include
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView

from models import *
from forms import *
from views import *

urlpatterns = [
    # Home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('icinema:cinema_list', kwargs={'extension': 'html'})),
        name='home_page'),

    #CINEMA

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

    # Create Cinemes
    url(r'^cinemes/create/$',CinemaCreate.as_view(),name='cinema_create'),

    # Edit cinemes details
    url(r'^cinemes/(?P<pk>\d+)/edit/$', LoginRequiredCheckIsOwnerUpdateView.as_view(model=Cinema,
                                                                                   form_class=CinemaForm),
       name='cinema_edit'),

    # Delete Cinema
    url(r'^cinemes/(?P<pk>\d+)/delete_cinema/$',
       LoginRequiredCheckIsOwnerDeleteView.as_view(model=Cinema),
       name='cinema-delete'),

    #FILMS

    # Cinemes films list
    url(r'^cinemes/(?P<pk>\d+)/films\.(?P<extension>(json|xml))$',
       FilmsList.as_view(),
       name='films_list'),

    # Cinemes films details
    url(r'^cinemes/(?P<pkr>\d+)/films/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
       FilmsDetail.as_view(),
       name='films_detail'),

    #Create url for edit details of films.
    url(r'^cinemes/(?P<pkr>\d+)/films/(?P<pk>\d+)/edit/$', LoginRequiredCheckIsOwnerUpdateView.as_view(model=Films,
                                                                                                      form_class=FilmEditForm), name='film_edit'),

    #Necessary for a return correct by edit parameters of films
    url(r'^cinemes/(?P<pk>\d+)/films/(\.(?P<extension>(json|xml)))?$',
       FilmsDetail.as_view(),
       name='films_detail'),


    # Create Films
    url(r'^cinemes/(?P<pkr>\d+)/films/create$', FilmCreate.as_view(), name='film_create'),

    # Delete Film,
    url(r'^cinemes/(?P<pk>\d+)/delete_film/$',
       LoginRequiredCheckIsOwnerDeleteView.as_view(model=Films),
       name='films-delete'),

    #PERFORMANCES

    # Create Performances (Hours, Sala )
    url(r'^performances/(?P<pkr>\d+)/films/(?P<pk>\d+)/add_performance$', PerformanceCreate.as_view(), name='performance_create'),

    # Delete Performance,
    url(r'^performances/(?P<pk>\d+)/delete_performance/$', LoginRequiredCheckIsOwnerDeleteView.as_view(model=FilmsPerfomances),
       name='performance-delete'),

    # Edit performances details
    url(r'^performances/(?P<pk>\d+)/edit/$', LoginRequiredCheckIsOwnerUpdateView.as_view(model=FilmsPerfomances,
                                                                                   form_class=PerformancesEditForm),
       name='performances_edit'),
    # Cinemes performances list
    url(r'^performances\.(?P<extension>(json|xml))$', PerformancesList.as_view(), name='performances_list'),

    # Cinemes performances detail
    url(r'^performances/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
       PerformancesDetail.as_view(), name='performances_detail'),



    #RESTful API
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/cinemes/$', APICinemaList.as_view(), name='cinema-list'),
    url(r'^api/cinemes/(?P<pk>\d+)/$', APICinemaDetail.as_view(), name='cinema-detail'),
    url(r'^api/films/$', login_required(APIFilmsList.as_view()), name='films-list'),
    url(r'^api/films/(?P<pk>\d+)/$', APIFilmsDetail.as_view(), name='films-detail'),
    url(r'^api/performances/$', APIPerformanceList.as_view(), name='performances-list'),
    url(r'^api/performances/(?P<pk>\d+)/$', APIPerformanceDetail.as_view(), name='performances-detail'),
]