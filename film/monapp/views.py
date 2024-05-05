from django.shortcuts import render
from .models import Film 
from django.views.generic import ListView
from django.http import HttpResponseRedirect

# Create your views here.


class filmListView(ListView):
    model = Film
    template_name = 'all_movies.html'
    context_object_name = 'films'
    
    queryset = Film.objects.all()

def search(request):
    if request.method == 'POST':
        search = request.POST['searched']
        films = Film.objects.filter(title__contains=search)
        return render(request, 'search_bar.html', {'films': films
                                                #    , 'search': search
                                                   })
    else:    
        return render(request, 'search_bar.html')