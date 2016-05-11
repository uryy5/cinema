from django.forms import ModelForm
from models import *

class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        exclude = ('user','date',)

class FilmEditForm(ModelForm):
    class Meta:
        model = Films
        exclude = ('user', 'cinema',)

class FilmCreateForm(ModelForm):
    class Meta:
        model = Films
        exclude = ('user', 'cinema',)

class PerformancesCreateForm(ModelForm):
    class Meta:
        model = FilmsPerfomances
        exclude = ('user', 'cinema','films')