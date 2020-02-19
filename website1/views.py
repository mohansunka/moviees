from django.shortcuts import render,redirect

# Create your views here.

from website1.forms import MovieForm
from website1.models import Movie


def index_view(request):
    return render(request, 'website1/index.html')


def add_movie_view(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(list_movie_view)
    return render(request, 'website1/addmovie.html', {'form': form})


def list_movie_view(request):
    movies_list = Movie.objects.all().order_by('-rating')
    return render(request, 'website1/listmovie.html', {'movies_list': movies_list})
