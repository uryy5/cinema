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
from django.utils import simplejson

from models import Cinema,Films,Performances, CinemaReview
from forms import Cinema
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
        'contentbody': 'Managing non legal funding since 2013'
        })
    output = template.render(variables)
    return HttpResponse(output)

def userpage(request, username):
    try:
        user = User.objects.get(user=username)
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

def cinemajson(request):
    user = request.user
    if not user:
        raise Http404('User not found.')
    cinema = user.sobre_set.all()
    cinemajson = []
    for s in cinema:
        sobre = dict()
        sobre["date"]=s.date.ctime()
        sobre["donor"]=s.user.name
        sobre["user"]=s.user.user
        cinemajson.append(sobre)


    return HttpResponse(simplejson.dumps(cinemajson),mimetype='application/json')


class CinemaList(ListView, ConnegResponseMixin):
    model = Cinema
    queryset = Cinema.objects.filter(date__lte=timezone.now()).order_by('date')[:5]
    context_object_name = 'latest_cinema_list'
    template_name = 'icinema/cinema_list.html'

class CinemaDetail(DetailView, ConnegResponseMixin):
    model = Cinema
    template_name = 'icinema/cinema_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CinemaDetail, self).get_context_data(**kwargs)
        return context

def review(request, pk):
    cinema = get_object_or_404(Cinema, pk=pk)
    review = CinemaReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        cinema=cinema)
    review.save()
    return HttpResponseRedirect(reverse('icinema:cinema_detail', args=(cinema.id,)))