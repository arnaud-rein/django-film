from django.shortcuts import render
from .models import Film 
from django.views.generic import ListView

# Create your views here.


class filmListView(ListView):
    model = Film
    template_name = 'all_movies.html'
    context_object_name = 'films'
    
    queryset = Film.objects.all()
