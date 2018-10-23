from django.conf.urls import url 
from django.urls import path, include
from . import views


urlpatterns = [
    url(r'^$', views.list_heroes, name = 'list_heroes'),
    path('<int:id>/', views.hero_detail , name = 'hero_detail'),
    path('items/', views.items_list, name = 'list_items'),
    path('items/<int:id>/',views.item_detail, name = 'item_detail'),
]