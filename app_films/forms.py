from django import forms
from .models import Film


class FilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = ('film_name', 'film_year')

    is_active = forms.BooleanField(required=False, label="Исключить год")
