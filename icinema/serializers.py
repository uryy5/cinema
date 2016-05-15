from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *

class CinemaSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='icinema:cinema-detail')
    films = HyperlinkedRelatedField(many=True, read_only=True, view_name='icinema:films-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Cinema
        fields = ('uri', 'name', 'cinema_url', 'address', 'city', 'postcode', 'stateOrProvince',
                  'country', 'telephone', 'user', 'date','films')


class FilmsSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='icinema:films-detail')
    cinema = HyperlinkedRelatedField(view_name='icinema:cinema-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Films
        fields = ('uri', 'tittle', 'genere_classification', 'RATING_CHOICES', 'rating', 'advisory_age', 'sipnosis',
                  'duration', 'autors', 'directors', 'user', 'cinema')


class PerformancesSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='icinema:films-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Performances
        fields = ('uri', 'time', 'avaiable', 'type', 'user', 'date')