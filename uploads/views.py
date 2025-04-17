from django.http import Http404
from django.shortcuts import render
from uploads.models import Movie

def movie(request,movie_id):
    movie=Movie.objects.get(pk=movie_id)
    if movie is not None:
        return render(request, 'movies/movies.html', {'movie1': movie})
    else:
        raise Http404("Movie does not exist")
   