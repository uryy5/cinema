from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import date

# Creaate your models here.
class Cinema (models.Model):
    name = models.TextField(blank=True, null=True)
    #id_cinema=models.IntegerField()
    cinema_url=models.URLField(blank=True,null=True)
    adress=models.TextField(blank=True,null=True)
    city = models.TextField(blank=True, null=True)
    postcode=models.IntegerField()
    stateOrProvince = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    telephone=models.IntegerField()
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('icinema:cinema_detail', kwargs={'pk': self.pk})

class Performances (models.Model):
    id_performance=models.IntegerField()
    time=models.IntegerField(blank=True,null=True)
    avaiable=models.TextField(blank=True,null=True)
    type=models.TextField(blank=True,null=True)
    date=models.DateField()

    def __unicode__(self):
        return u"%s" % self.id_performance
    def get_absolute_url(self):
        return reverse('icinema:performances_detail', kwargs={'pk': self.pk})

class Films (models.Model):
    id_film=models.IntegerField()
    title=models.TextField(blank=True,null=True)
    classification=models.TextField(blank=True,null=True)
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Classificacio', blank=False, default=3, choices=RATING_CHOICES)
    advisory_age=models.IntegerField()
    sipnosis=models.TextField(blank=True,null=True)
    duration=models.IntegerField()
    autors=models.TextField(blank=True,null=True)
    directors=models.TextField(blank=True,null=True)

    def __unicode__(self):
        return u"%s" % self.id_film
    def get_absolute_url(self):
        return reverse('icinema:film_detail', kwargs={'pk': self.pk})
