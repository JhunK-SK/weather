from django.urls import path, include
from . import views


urlpatterns = [
    # Home Page
    path('', views.index, name='home'),
]