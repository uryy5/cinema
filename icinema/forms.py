from django.forms import ModelForm
from models import Cinema

class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        exclude = ('name',)

