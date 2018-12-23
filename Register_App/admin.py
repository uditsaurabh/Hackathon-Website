from django.contrib import admin

# Register your models here.
from .models import Team,Participants

# Register your models here.
admin.site.register(Team)
admin.site.register(Participants)
