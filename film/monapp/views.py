from django.shortcuts import render
import requests
from .models import Film 
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from urllib.parse import quote

# Create your views here.

class filmListView(ListView):
    """
    Voir la liste des films enregistrés dans la base de données
    """
    model = Film
    template_name = 'all_movies.html'
    context_object_name = 'films'
    
    queryset = Film.objects.all()


def search(request):
    """ 
    Rechercher un film par son titre via la requête POST 
    On va utiliser la _icontains pour filter les films qui contiennent le mot recherché
    """
    if request.method == 'POST':
        
        searched = request.POST['searched']
        films = Film.objects.filter(title__icontains=searched) 
        print("films => ")
        print(films)
        
        """
        Si le film n'existe pas dans la base de données, on va le chercher dans l'api
        et le rentrer en bdd
        """
        if not films.exists():
            data = get_movie_data(searched)
            
            if data is not None:

                Film.objects.create(title=data['Title'],
                                    year=data['Year'],
                                    style=data['Genre'],
                                    director=data['Director'],           
                                    description=data['Plot'])
                
                return render(request, 'search_bar.html', {'movies': data})
            else:
                return render(request, 'error_template.html', {'error': 'Failed to retrieve data'})
        return render(request, 'search_bar.html', {'films': films, 'searched': searched})
    else:
        return render(request, 'search_bar.html', {})    
    

def film_detail(request, film_id):
    """
    Recherche d'un film par son id
    """
    film = Film.objects.get(id=film_id)
    return render(request, 'film_detail.html', {'film': film})



def get_movie_data(title):

    """ 
    Récupérer les informations de l'api omdbapi.com
    """
    try:
        title = quote(title)
        url = f"https://www.omdbapi.com/?t={title}&apikey=5e975dd0"
        response = requests.get(url)
        print("api rsponse => " +  response.text) 
        response.raise_for_status()  
        return response.json()
    except requests.RequestException as e:
        print(e)
        return None



def movie_view(request, title):

    """
    voir les informations d'un film
    """
    try:
        film = Film.objects.get(title=title)
        return render(request, 'film_detail.html', {'film': film})
    except Film.DoesNotExist:
        data = get_movie_data(title)
        if data is not None:
            return render(request, 'movie_api.html', {'movies': data})
        else:
            return render(request, 'error_template.html', {'error': 'Failed to retrieve data'})
        

def homepage(request):
    """
    Page d'accueil
    """
    return render(request, 'homepage.html', {})