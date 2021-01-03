from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import CityForm

def index(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}"
    api_key = "3305a1cea0761d956da3c5f87c21b563"
    
    form = CityForm()
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            typed_city = form.cleaned_data["name"]
            print(typed_city)
            count_type_city = City.objects.filter(name=typed_city).count()
            print(count_type_city)
            if count_type_city == 0:
                r = requests.get(url.format(typed_city, api_key)).json()
                if r["cod"] == 200:
                    form.save()
                    return redirect("home")
    
    cities = City.objects.all().order_by('-created_date')
    city_data = []
    for city in cities:
        
        r = requests.get(url.format(city, api_key)).json()
        weather_data = {
            "id": city.id,
            "city": r["name"],
            "country": r["sys"]["country"],
            "description": r["weather"][0]["description"],
            "icon": r["weather"][0]["icon"],
            "temp": "{:.1f}".format(r["main"]["temp"]),
            "feelslike": "{:.1f}".format(r["main"]["feels_like"]),
        }
        city_data.append(weather_data)
    
    context = {
        "city_data": city_data,
        "form": form,
        }
    return render(request, 'weather/index.html', context)


def delete_city(request, city_id):
    City.objects.get(pk=city_id).delete()
    return redirect('home')

def delete_all_cities(request):
    City.objects.all().delete()
    return redirect('home')