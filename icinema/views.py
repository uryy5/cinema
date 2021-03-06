from django.shortcuts import render
from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, DeleteView,UpdateView
from django.views.generic.edit import CreateView
from django.core import serializers
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.generic.base import TemplateResponseMixin
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from forms import *
from serializers import CinemaSerializer, FilmsSerializer, PerformancesSerializer,CinemaReviewSerializer

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'icinema/form.html'

class LoginRequiredCheckIsOwnerDeleteView(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    template_name = 'icinema/delete_object.html'
    success_url = "/icinema"

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

    def get_context_data(self, **kwargs):
        context = super(CinemaDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = Review.RATING_CHOICES
        return context



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
    template_name = 'icinema/performances_detail.html'




class CinemaCreate(LoginRequiredMixin,CreateView):
    model = Cinema
    template_name = 'icinema/form.html'
    form_class = CinemaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CinemaCreate, self).form_valid(form)

class FilmCreate(LoginRequiredMixin,CreateView):
    model = Films
    template_name = 'icinema/form.html'
    form_class = FilmCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.cinema = Cinema.objects.get(id=self.kwargs['pkr'])
        return super(FilmCreate, self).form_valid(form)

class PerformanceCreate(LoginRequiredMixin,CreateView):
    model = FilmsPerfomances
    template_name = 'icinema/form.html'
    form_class = PerformancesCreateForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.films = Films.objects.get(id=self.kwargs['pk'])
        return super(PerformanceCreate, self).form_valid(form)

class ReviewCreate(LoginRequiredMixin, CreateView):
    model = CinemaReview
    template_name = 'icinema/form.html'
    form_class = CinemaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReviewCreate, self).form_valid(form)

@login_required()
def review(request, pk):
    cinema = get_object_or_404(Cinema, pk=pk)
    review = CinemaReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        cinema=cinema)
    review.save()
    return HttpResponseRedirect(reverse('icinema:cinema_detail', args=(cinema.id,)))




### RESTful API views ###

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user

class APICinemaList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Cinema
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

class APICinemaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Cinema
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

class APIFilmsList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Films
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer

class APIFilmsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Films
    queryset = Films.objects.all()
    serializer_class = FilmsSerializer

class APIPerformanceList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = FilmsPerfomances
    queryset = FilmsPerfomances.objects.all()
    serializer_class = PerformancesSerializer

class APIPerformanceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = FilmsPerfomances
    queryset = FilmsPerfomances.objects.all()
    serializer_class = PerformancesSerializer

class APICinemaReviewList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = CinemaReview
    queryset = CinemaReview.objects.all()
    serializer_class = CinemaReviewSerializer

class APICinemaReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = CinemaReview
    queryset = CinemaReview.objects.all()
    serializer_class = CinemaReviewSerializer


