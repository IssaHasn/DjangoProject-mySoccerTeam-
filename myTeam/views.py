from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Players

def team(request):
    teamPlayers = Players.objects.all()
    context = {
        'Team':teamPlayers
    }
    template = loader.get_template('myTeam.html')
    return HttpResponse(template.render(context, request))

def player(request, id):
    playerData = Players.objects.get(id = id)
    context = {
        'player':playerData
    }
    template = loader.get_template("player.html")
    return HttpResponse(template.render(context,request))

def login(request):
    name = request.POST.get('name')
    lastName = request.POST.get('lastName')
    age = request.POST.get('age')
    phone = request.POST.get('phone')
    
    dataList = [name, lastName, age, phone]
    
    template = loader.get_template("login.html")
    return HttpResponse(template.render())

    while True:
        for data in dataList:
            if data == "":
                break
            else:
                pass
        Login = Players(name = name, lastName = lastName, age = age, phoneNumber = phone)
        Login.save()
        break
