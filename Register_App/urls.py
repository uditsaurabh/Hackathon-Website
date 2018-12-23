from django.contrib import admin
from django.urls import path
from .views import home,register,juryLogin,jurydisplay,juryLogout,jurydataUpdate,participants,ListParticipants
from django.views.generic.base import TemplateView
urlpatterns = [
    path('home', home,name='home'),
    path('register',register,name='register'),
    path('juryLogin',juryLogin,name='juryLogin'),
    path('jd',jurydisplay,name='jurydisplay'),
    path('juryLogout', juryLogout, name='juryLogout'),
    path('jurydataUpdate', jurydataUpdate, name='jurydataUpdate'),
    path('participants',participants,name='participants'),
    # path('participants/rest',ListParticipants.as_view()),
]
