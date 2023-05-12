from django.shortcuts import render
from .models import director, movie

# Create your views here.

def home(request):

    directors = director.objects.all()
    return render(request, 'home.html', {'directors': directors})

def movies(request, id):

    director_obj = director.objects.get(id=id)
    movies = movie.objects.filter(director=director_obj)

    return render(request, 'movies.html', {'movies' : movies})