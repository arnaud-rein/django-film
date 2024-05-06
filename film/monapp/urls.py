from django.urls import path
from . import views
from .views import filmListView




urlpatterns = [
    path("/", filmListView.as_view(), name="movie"),
    path("/search", views.search, name="search"),
    path("/api", views.movie_view, name="api"),
    path('film/<int:film_id>/', views.film_detail, name='film_detail'),
    path('film/<str:title>/', views.movie_view, name='film_name'),
   
  
]