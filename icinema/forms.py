from django.forms import ModelForm
from models import *

class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        exclude = ('user','date')

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

class PerformancesEditForm(ModelForm):
    class Meta:
        model = FilmsPerfomances
        exclude = ('user','films','cinema')

class ReviewEditForm(ModelForm):
    class Meta:
        model = Review
        exclude = ('user','date')