from django.forms import ModelForm
from models import Cinema, Films

class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        exclude = ('user',)

class FilmForm(ModelForm):
    class Meta:
        model = Films
        exclude = ('user', 'cinema', 'tittle',)

