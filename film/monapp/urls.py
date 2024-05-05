from django.urls import path
from . import views
from .views import filmListView




urlpatterns = [
    path("/", filmListView.as_view(), name="movie"),
    path("/search", views.search, name="search"),
    path('film/<int:film_id>/', views.film_detail, name='film_detail'),
   
  
]