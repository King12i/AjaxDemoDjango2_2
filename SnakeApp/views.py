from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import *

# Create your views here.


def index(request):
    context = {
        'all_snakes': Snake.objects.all()
    }
    return render(request, 'index.html', context)


def snakeForm(request):
    return render(request, 'snakeform.html')


def addSnake(request):
    if('venomous' in request.POST):
        ven = True
    else:
        ven = False
    errors = Snake.objects.snake_validate(request.POST)
    if len(errors) > 0:
        for tags, value in errors.items():
            messages.error(request, value, extra_tags=tags)
        return JsonResponse({ 'status': 'error' })
    
    return JsonResponse({ 'status': 'success' })


def oneSnake(request, snake_id):
    context = {
        'snake': Snake.objects.get(id=snake_id)
    }
    return render(request, 'onesnake.html', context)


def allSnakes(request):
    context = {
        'all_snakes': Snake.objects.all()
    }
    return render(request, "allsnakes.html", context)


def deleteSnake(request, snake_id):
    Snake.objects.get(id=snake_id).delete()
    return redirect("/snakes/all")