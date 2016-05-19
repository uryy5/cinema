from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Cinema (models.Model):
    name = models.TextField()
    cinema_url=models.URLField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    city = models.TextField(blank=True, null=True)
    postcode=models.IntegerField()
    stateOrProvince = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    telephone=models.IntegerField()
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="icinema", blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('icinema:cinema_detail', kwargs={'pk': self.pk})

class Films (models.Model):
    tittle=models.TextField(blank=True,null=True)
    genere_classification=models.TextField(blank=True,null=True)
    RATING_CHOICESS = ((1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'))
    ratingg = models.PositiveSmallIntegerField('Rating', blank=False, default=3, choices=RATING_CHOICESS)
    advisory_age=models.IntegerField()
    sipnosis=models.TextField(blank=True,null=True)
    duration=models.IntegerField()
    autors=models.TextField(blank=True,null=True)
    directors=models.TextField(blank=True,null=True)
    user= models.ForeignKey(User,default=1)
    cinema=models.ForeignKey(Cinema,null=True, related_name='films')
    image = models.ImageField(upload_to="icinema", blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.tittle
    def get_absolute_url(self):
        return reverse('icinema:films_detail', kwargs={'pk': self.pk})


class Performances(models.Model):
    time = models.TimeField(blank=True,null=True)
    avaiable = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.type

    def get_absolute_url(self):
        return reverse('icinema:films_detail', kwargs={'pkr': self.films.cinema.pk, 'pk':self.films.pk, 'extension': 'html'})

class FilmsPerfomances(Performances):
    films = models.ForeignKey(Films)

class Review(models.Model):
    RATING_CHOICES = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField()
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class CinemaReview(Review):
    cinema = models.ForeignKey(Cinema)

    def get_absolute_url(self):
        return '/icinema/cinemes/' + str(self.cinema.id) + '.html'