from tastypie.resources import ModelResource
from wiki.models import Hero, Item

class HeroResource(ModelResource):
    class Meta:
        queryset = Hero.objects.all()
        resource_name = 'hero'

class ItemResource(ModelResource):
    class Meta:
        queryset = Item.objects.all()
        resource_name = 'item'