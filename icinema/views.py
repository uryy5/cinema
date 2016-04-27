from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView
from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
#from django.utils import simplejson

from models import Cinema,Films,Performances,FilmsPerfomances
from forms import CinemaForm
# Create your views here.


class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        return super(ConnegResponseMixin, self).render_to_response(context)


def mainpage(request):
    template = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'Cinema aPP',
        'pagetitle': 'Welcome to the Cinema aPPlication',
        'contentbody': 'Managing non legal funding since 2013',
        'user': request.user
        })
    output = template.render(variables)
    return HttpResponse(output)

def userpage(request, username):
    try:
        user = User.objects.get(id=username)
    except:
        raise Http404('User not found.')

    cinema = user.sobre_set.all()
    template = get_template('userpage.html')
    variables = Context({
        'user': user,
        'cinema': cinema
        })
    output = template.render(variables)
    return HttpResponse(output)

class CinemaList(ListView, ConnegResponseMixin):
    model = Cinema
    queryset = Cinema.objects.all()
    context_object_name = 'cinema_list'
    template_name = 'icinema/cinema_list.html'

class CinemaDetail(DetailView, ConnegResponseMixin):
    model = Cinema
    queryset = Cinema.objects.all()
    template_name = 'icinema/cinema_detail.html'

class FilmsList(ListView, ConnegResponseMixin):
    model = Films
    queryset = Films.objects.all()


class FilmsDetail(DetailView, ConnegResponseMixin):
    model = Films
    template_name = 'icinema/films_detail.html'

class PerformancesList(ListView, ConnegResponseMixin):
    model = Performances
    queryset = Performances.objects.all()


class PerformancesDetail(DetailView, ConnegResponseMixin):
    model = Performances
    queryset = Performances.objects.all()
    template_name = 'icinema/films_detail.html'

def performances(request, pk):
    films = get_object_or_404(Films, pk=pk)
    performances = FilmsPerfomances(
        user=request.user,
        films=films)
    performances.save()
    return HttpResponseRedirect(reverse('icinema:films_detail', args=(films.id,)))

class CinemaCreate(CreateView):
    model = Cinema
    template_name = 'icinema/form.html'
    form_class = CinemaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CinemaCreate, self).form_valid(form)