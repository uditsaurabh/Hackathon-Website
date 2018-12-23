from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Team(models.Model):
    Theme_Choices=(
        ('Prevention','Prevention'),
        ('Detection','Detection'),
        ('Resolution','Resolution'),
        ('UserInterface','UserInterface'),
        ('Commercial','Commercial'),
        ('DeliveryModel','DeliveryModel')
    )
    teamName=models.CharField(max_length=200)
    usecase=models.TextField()
    creation=models.DateTimeField(auto_now=True)
    score=models.IntegerField(default=0)
    theme=models.CharField(max_length=50,choices=Theme_Choices,default='Commercial')
    title_desc=models.CharField(max_length=300)
    # email=models.CharField(max_length=100)
    idea_detail=models.TextField()
    High_Level_Design=models.TextField()
    detailed_design=models.TextField()
    solution_platform=models.TextField()
    usd_Cost_To_Implement=models.IntegerField()
    usd_benefits_perannum=models.IntegerField()
    benefits=models.TextField()
    has_idea_implemented_anywhere=models.TextField()

    def __str__(self):
        return self.teamName
    def __repr__(self):
        return str(self.id)



class Participants(models.Model):

    creation = models.DateTimeField(auto_now_add=True)

    Team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
    email=models.CharField(max_length=200,default='X')
    def __str__(self):
        return self.email
    def __repr__(self):
        return  str(self.email)
