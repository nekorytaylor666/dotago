from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Hero
from django.db.models import Q
import os 
import glob
# Create your views here.

def list_heroes(request):
    heroes = Hero.objects.all()
    images = get_heroes_images()
    context = {
        "images" : images,
        "heroes" : heroes
    }
    return render(request, "index.html", context)

def get_heroes_images():
    directory = "static/hero-icons/"
    files = os.listdir(directory)
    for item in files:
        print(item)
    return files
    
def hero_detail(request, id=None):
    instance = get_object_or_404(Hero, id=id)
    context_data = {
        "hero": instance,
    }

    return render(request, "hero_detail.html", context_data)

def heroes_images_fill():
    directory = "static/hero-icons/"
    for icon in os.listdir(directory):
        name = icon.replace('_icon.png','').replace('_',' ')
        new_hero = Hero(name = name, hero_icon = icon)
        new_hero.save()
        # print(name)
