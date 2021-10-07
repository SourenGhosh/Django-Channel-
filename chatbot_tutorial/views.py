from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from chatbot_tutorial.models import ButtonTracker
from django.db.models import F

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@csrf_exempt
def chat(request):
    print("jnd")
    context = {}
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            user=request.user
            print("hi")
            return render(request, 'chatbot_tutorial/chatbot.html', context)
    return render(request, "chatbot_tutorial/loginpage.html")
# def chat(request):
#     context = {}
#     return render(request, 'chatbot_tutorial/chatbot.html', context)

def html_table(request):
    button_clicker=ButtonTracker.objects.all().values('user__username', 'fat_count', 'stupid_count', 'dumb_count')
    cont=list(button_clicker)
    return render(request, "chatbot_tutorial/table.html", {'pass_cont': cont})

def respond_to_websockets(message):
    jokes = {
     'stupid': ["""Yo' Mama is so stupid, she needs a recipe to make ice cubes.""",
                """Yo' Mama is so stupid, she thinks DNA is the National Dyslexics Association."""],
     'fat':    ["""Yo' Mama is so fat, when she goes to a restaurant, instead of a menu, she gets an estimate.""",
                """ Yo' Mama is so fat, when the cops see her on a street corner, they yell, "Hey you guys, break it up!" """],
     'dumb':   ["""Yo' Mama is so dumb, when God was giving out brains, she thought they were milkshakes and asked for extra thick.""",
                """Yo' Mama is so dumb, she locked her keys inside her motorcycle."""] 
     }  
    result_message = {
        'type': 'text'
        }
    u_ins = User.objects.get(username=message['user'])
    button_query, status=ButtonTracker.objects.get_or_create(user=u_ins)
    if 'fat' in message['text']:
        print("fat")
        button_query.fat_count=F('fat_count')+1
        button_query.save()
        result_message['text'] = random.choice(jokes['fat'])
    
    elif 'stupid' in message['text']:
        button_query.stupid_count=F('stupid_count')+1
        button_query.save()
        result_message['text'] = random.choice(jokes['stupid'])
    
    elif 'dumb' in message['text']:
        button_query.dumb_count=F('dumb_count')+1
        button_query.save()
        result_message['text'] = random.choice(jokes['dumb'])

    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message.update({'type': 'arr'})
        result_message['text'] = "Hello to you too! If you're interested in yo mama jokes, just tell me fat, stupid or dumb and i'll tell you an appropriate joke."
    else:
        result_message.update({'type': 'arr'})
        result_message['text'] = ["fat", 'stupid', 'dumb']

    return result_message
    