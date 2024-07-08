from django.contrib import admin
from .models import Tournament, Round, Match, Player, MyApply

admin.site.register(Tournament)
admin.site.register(Round)
admin.site.register(Match)
admin.site.register(Player)
admin.site.register(MyApply)

