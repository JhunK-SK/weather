from django.urls import path, include
from . import views


urlpatterns = [
    # Home Page.
    path('', views.index, name="home"),
    
    # Delete seleted city.
    path('delete_city/<city_id>/', views.delete_city, name="delete_city"),
    
    # Delete all cities.
    path('delete_all/', views.delete_all_cities, name="delete_all_cities"),
]