
from django.db import models


# Create your models here.
class Film(models.Model):
    film_name = models.CharField(max_length=40, verbose_name='название фильма', blank=True)
    film_country = models.CharField(max_length=40, verbose_name='страна', blank=True)
    film_year = models.IntegerField(verbose_name='год', blank=True)

