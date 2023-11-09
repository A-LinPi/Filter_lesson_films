from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('film_name', 'film_country', 'film_year')
