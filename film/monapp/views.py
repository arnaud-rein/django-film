from django.shortcuts import render
import requests
from .models import Film 
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from urllib.parse import quote

# Create your views here.


class filmListView(ListView):
    model = Film
    template_name = 'all_movies.html'
    context_object_name = 'films'
    
    queryset = Film.objects.all()

# def search(request):
#     if request.method == 'POST':
#         search = request.POST['searched']
#         films = Film.objects.filter(title__contains=search)
#         return render(request, 'search_bar.html', {'films': films})    

#     else:    
#         return render(request, 'search_bar.html')   


def search(request):
    if request.method == 'POST':
        print('dans le post')
        searched = request.POST['searched']
        films = Film.objects.filter(title__icontains=searched)
        print("films => ")
        print(films)
        if not films.exists():
            data = get_movie_data(searched)
            print("data=>")
            print(data)
            if data is not None:
                return render(request, 'movie_api.html', {'movies': data})
            else:
                return render(request, 'error_template.html', {'error': 'Failed to retrieve data'})
        return render(request, 'search_bar.html', {'films': films, 'searched': searched})
    else:
        return render(request, 'search_bar.html', {})    
    

def film_detail(request, film_id):
    film = Film.objects.get(id=film_id)
    return render(request, 'film_detail.html', {'film': film})



def get_movie_data(title):
    try:
        title = quote(title)
        url = f"https://www.omdbapi.com/?t={title}&apikey=5e975dd0"
        response = requests.get(url)
        print("api rsponse => " +  response.text) 
        response.raise_for_status()  # Lève une exception pour les codes 4XX ou 5XX
        return response.json()
    except requests.RequestException as e:
        print(e)
        return None


# def movie_view(request, title):
#     data = get_movie_data()
#     if data is not None:
#         return render(request, 'movie_api.html', {'movies': data})
#     else:
#         return render(request, 'error_template.html', {'error': 'Failed to retrieve data'})
    

def movie_view(request, title):
    try:
        film = Film.objects.get(title=title)
        return render(request, 'film_detail.html', {'film': film})
    except Film.DoesNotExist:
        data = get_movie_data(title)
        if data is not None:
            return render(request, 'movie_api.html', {'movies': data})
        else:
            return render(request, 'error_template.html', {'error': 'Failed to retrieve data'})