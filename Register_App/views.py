from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect
from .models import Participants,Team
from django.db import transaction,IntegrityError
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from .serializers import TeamSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
def home(request):
    return render(request, 'home.html')

class ListParticipants(ListAPIView):
    serializer_class = TeamSerializers
    queryset = (Team.objects.all().order_by('id'))
#
# def participants(request):
#     print("this is request")
#     return render(request, "ParticipantsRest.html", {})

def participants(request):
    team=(Team.objects.all().order_by('id')).all()
    print(team)
    print(team.all())
    for t in team:
        print( t.participants_set)
    return render(request,"Participants.html",{'team':team})

def register(request):
    if request.method == 'GET':
        print('register is getting called correctly from submit')
        return render(request,'RegistrationForm.html')
    if request.method == 'POST':
        print('POST is getting called correctly from submit')
        queryParameter=request.POST
        teamname=queryParameter.get("TeamName")
        theme=queryParameter.get("Theme")
        PrimaryEmail=queryParameter.get("EmailAddress")
        Email1 = queryParameter.get("EmailAddress1")
        Email2 = queryParameter.get("EmailAddress2")
        ideatitle=queryParameter.get("ideatitle")
        ideadetail=queryParameter.get("ideadetail")
        hld=(queryParameter.get("HighLevelDesign"))
        dd=queryParameter.get("detaileddesign")
        sp=queryParameter.get("solutionplatform")
        costToImplement=queryParameter.get("usdcosttoimplement")
        benefits=queryParameter.get("usdbenefits")
        benefitAnalysis=queryParameter.get("benefits")
        ideaImplemented=queryParameter.get("ideaImplementedAnywhere")

        l=[]
        team = Team(teamName=teamname,theme=theme,title_desc=ideatitle,idea_detail=ideadetail,
        High_Level_Design=hld,detailed_design=dd,solution_platform=sp,usd_Cost_To_Implement=costToImplement,
        usd_benefits_perannum=benefits,benefits=benefitAnalysis,
        has_idea_implemented_anywhere='ideaImplemented')

        p_main=Participants(email=PrimaryEmail,Team=team)
        l.append(team,p_main)
        if Email1 is not None:
            p_1=Participants(email=Email1,Team=team)
            l.append(p_1)
        if Email2 is not None:
            p_2=Participants(email=Email2,Team=team)
            l.append(p_2)
        try:
            with transaction.atomic():
                for p in l:
                    p.save()
        except IntegrityError as i:
                print(i)

        return render(request,'RegistrationForm.html',{'sucess':True})

def juryLogin(request):
    context={}
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('jurydisplay'))
        else:
            context["error"]="Provide valid credential details"
            return render(request,'juryLogin.html',context)
    else:

        return render(request, 'juryLogin.html', context)


def juryLogout(request):
    print("loggedout")
    logout(request)
    return render(request,"home.html",{})
@login_required
def jurydisplay(request):
    if request.method=='GET':
        return render(request,'jurydisplay.html',{'display':False})
    else:
        team=request.POST.get("TeamName")
        lst=(Team.objects.filter(teamName=team))
        if len(lst)>0:
            team=lst[0]
            return render(request, 'jurydisplay.html', {'display':True,'team':team})
        else:
            return render(request, 'jurydisplay.html', {'display': False, 'team': team})
def jurydataUpdate(request):
    print("hey")
    teamname=request.POST.get('teamname')
    teamrating=request.POST.get('teamrating')
    team = (list(Team.objects.filter(title=teamname)))[0]
    team.rating=int(teamrating)
    team.save()
    return JsonResponse({})