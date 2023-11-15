from django.shortcuts import render
from .models import Film
from .forms import FilmForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def film(request):
    forma = FilmForm
    db = {}
    if request.POST:
        K1 = request.POST.get('film_name')
        K2 = request.POST.get('film_year')
        is_active = request.POST.get('is_active')
        if K1:
            db = Film.objects.filter(film_name=K1)
        elif K2 and is_active:
            db = Film.objects.exclude(film_year=K2)
        elif K2:
            db = Film.objects.filter(film_year=K2)

    data = {'forma': forma, 'database': db}
    return render(request, 'films.html', data)
