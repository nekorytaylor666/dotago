from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Hero,Item
from django.db.models import Q
import os 
import glob
# Create your views here.

def list_heroes(request):
    heroes = Hero.objects.all()
    context = {
        "heroes" : heroes
    }
    
    return render(request, "hero_list.html", context)

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

        
def item_detail(request, id=None):
    instance = get_object_or_404(Item, id=id)
    context_data = {
        "item": instance,
    }

    return render(request, "item_detail.html", context_data)

def heroes_images_fill():
    directory = "static/hero-icons/"
    for icon in os.listdir(directory):
        name = icon.replace('_icon.png','').replace('_',' ')
        new_hero = Hero(name = name, hero_icon = icon)
        new_hero.save()
        # print(name)

def items_images_fill():
    directory = "static/items-icons/complex/"
    for icon in os.listdir(directory):
        name = icon.replace('_icon.png','').replace('_',' ')
        new_item = Item(name = name, hero_icon = icon)
        new_item.save()

def items_list(request):
    items = Item.objects.all()
    context = {
        "items" : items
    }
    return render(request, "items_list.html", context)
    

