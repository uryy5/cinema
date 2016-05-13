from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from icinema.models import Cinema

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
#from django.utils import simplejson


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions
from models import Performances, Cinema, Films
from serializers import CinemaSerializer, FilmSerializer, PerformancesSerializer
from forms import *
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

class FilmCreate(CreateView):
    model = Films
    template_name = 'icinema/form.html'
    form_class = FilmCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.cinema = Cinema.objects.get(id=self.kwargs['pkr'])
        return super(FilmCreate, self).form_valid(form)

class PerformanceCreate(CreateView):
    model = FilmsPerfomances
    template_name = 'icinema/form.html'
    form_class = PerformancesCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.films = Films.objects.get(id=self.kwargs['pk'])
        return super(PerformanceCreate, self).form_valid(form)

class DeleteCinemaView(DeleteView):
    model = Cinema
    template_name = 'icinema/delete_cinema.html'

    def get_success_url(self):
        return reverse('icinema:cinema_list' , kwargs={'extension': 'html' })

class DeleteFilmView(DeleteView):
    model = Films
    template_name = 'icinema/delete_film.html'

    def get_success_url(self):
        return reverse('icinema:cinema_list', kwargs={ 'extension': 'html'})

class DeletePerformanceView(DeleteView):
    model = Performances
    template_name = 'icinema/delete_performance.html'

    def get_success_url(self):
        return reverse('icinema:cinema_list', kwargs={'extension': 'html'})

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user

class APICinemaList(generics.ListCreateAPIView):
    model = Cinema
    serializer_class = CinemaSerializer

class APICinemaDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Cinema
    serializer_class = CinemaSerializer

class APIFilmList(generics.ListCreateAPIView):
    model = Films
    serializer_class = FilmSerializer

class APIFilmDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Films
    serializer_class = FilmSerializer

class APIPerformancesList(generics.ListCreateAPIView):
    model = Performances
    serializer_class = PerformancesSerializer

class APIPerformancesDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Performances
    serializer_class = PerformancesSerializer


