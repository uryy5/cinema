from django.shortcuts import render

from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView

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
    output = '''
        <html>
        <head><title>%s</title></head>
        <body>
        <h1>%s</h1><p>%s</p>
        </body>
        </html>
        ''' % ( 'Cinema aPP',
        'Welcome to the Cinema aPPlication',
        'Cinema app ')
    return HttpResponse(output)

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