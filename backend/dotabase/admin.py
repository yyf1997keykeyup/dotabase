from django.contrib import admin

# Register your models here.
from dotabase.models import *

admin.site.register(Hero)
admin.site.register(HeroBadAgainst)
admin.site.register(HeroGoodAgainst)
admin.site.register(HeroBestCombos)