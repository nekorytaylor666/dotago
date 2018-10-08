from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length = 200)
    
    hero_icon = models.CharField(max_length = 50)

    hero_description = models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tincidunt quam ut justo tristique laoreet. Mauris vel orci porttitor, vehicula risus eu, posuere arcu. Nulla facilisi. Sed malesuada augue id orci ullamcorper aliquam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras iaculis ante sed nisi sagittis, a venenatis justo rhoncus. Pellentesque at mauris quis tortor scelerisque gravida eget et velit. Aliquam erat volutpat. Duis varius neque sapien, nec tincidunt mauris molestie et. Nunc feugiat nibh vitae tortor facilisis efficitur. Proin ut venenatis lectus. Ut id imperdiet ligula, eu luctus turpis.')

    hero_short_description = models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tincidunt quam ut justo tristique laoreet. Mauris vel orci porttitor, vehicula risus eu, posuere arcu. Nulla facilisi. Sed malesuada augue id orci ullamcorper aliquam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras iaculis ante sed nisi sagittis, a venenatis justo rhoncus. Pellentesque at mauris quis tortor scelerisque gravida eget et velit. Aliquam erat volutpat. Duis varius neque sapien, nec tincidunt mauris molestie et. Nunc feugiat nibh vitae tortor facilisis efficitur. Proin ut venenatis lectus. Ut id imperdiet ligula, eu luctus turpis.')
    
    basic_stren = models.IntegerField(default=0)
    basic_agil = models.IntegerField(default=0)
    basic_intel = models.IntegerField(default=0)

    stren_gain = models.FloatField(default=0)
    agil_gain = models.FloatField(default=0)
    intel_gain = models.FloatField(default=0)

    health = models.IntegerField(default=0)
    mana = models.IntegerField(default=0)
    damage = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    armor = models.IntegerField(default=0)

    attack_distance = models.IntegerField(default=150)
    attack_speed = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Abilities(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(default='Призывает фантома, который летит к выбранной цели и сжимает её в своих объятьях, \nнанося периодический урон и запрещая применять способности. Если фантом продержится на жертве до конца действия,\n он нанесёт ей большой урон от разрыва и вернётся к владельцу, а время перезарядки способности сбросится.\nОдна геройская атака по фантому считается за три обычных.')
    hero = models.ForeignKey(Hero,  on_delete=models.CASCADE)
    def __str__(self):
        return self.name



  


    


    