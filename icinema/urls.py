from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView

#from models import Films
#from forms import CinemaForm
from views import CinemaDetail, CinemaList

urlpatterns = patterns('',
    # Home page
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('icinema:cinema_list', kwargs={'extension': 'html'})),
        name='home_page'),

    # List cinemes: /icinema/cinemes.json or html or xml
    url(r'^cinemes\.(?P<extension>(json|xml|html))$',
        CinemaList.as_view(),
        name='cinema_list'),

    url(r'^cinemes/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        CinemaDetail.as_view(),
        name='cinema_detail'),
)