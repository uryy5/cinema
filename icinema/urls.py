from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView

#from models import Films
#from forms import CinemaForm
from views import CinemaDetail, CinemaList

urlpatterns = patterns('',
    # Home page
    url(r'^$', mainpage, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^icinema/ ', include('icinema.urls', namespace='icinema'))

)