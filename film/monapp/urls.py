from django.urls import path
from . import views
from .views import filmListView




urlpatterns = [
    path("/", filmListView.as_view(), name="movie"),
   
  
]