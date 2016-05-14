from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Cinema, Films, Performances

class CinemaSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='cinema:cinema-detail')
    films = HyperlinkedRelatedField(many=True, read_only=True, view_name='cinema:films-detail')
    performances_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='cinema:films-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Cinema
        fields = ('url', 'name', 'cinema_url', 'address', 'city', 'postcode', 'stateOrProvince',
                  'country', 'telephone', 'user', 'date', 'dishes', 'performances_set')


class FilmSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='cinema:films-detail')
    cinema = HyperlinkedRelatedField(view_name='cinema:cinema-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Films
        fields = ('url', 'tittle', 'genre_classification', 'RATING_CHOICES', 'rating', 'advisory_age', 'sipnosis',
                  'duration', 'autors', 'directors', 'user', 'cinema')


class PerformancesSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='cinema:films-detail')
    cinema = HyperlinkedRelatedField(view_name='cinema:cinema-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Performances
        fields = ('url', 'time', 'avaiable', 'type', 'user', 'date', 'cinema')