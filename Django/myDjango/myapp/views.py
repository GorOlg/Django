import random

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    html_main = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Добро пожаловать на мой сайт!</title>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django сайт!</h1>
        <p>Здесь вы найдете удивительные и вдохновляющие идеи.</p>
    </body>
    </html>
    """
    return HttpResponse(html_main)


def about(request):
    return HttpResponse('about me')


def change(request):
    x = ['орел', 'решка']
    random_item = random.choice(x)
    return HttpResponse(random_item)


def result_no(request):
    x = [1, 2, 3, 4, 5, 6]
    random_item = random.choice(x)
    return HttpResponse(random_item)


def ugad(request):
    x = random.randint(0, 100)
    return HttpResponse(x)


def autobiography(request):
    text = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>О creator</title>
    </head>
    <body>
        <h1>Привет, я Олег!</h1>
        <p>Я - человек с необычными взглядами на жизнь и огромным энтузиазмом к творчеству.</p>
        <p>Мои идеи каталитично взрываются в моей голове и жаждут реализации.</p>
        <p>В моем сердце живет пламя страсти к жизни и жажде познания.</p>
    </body>
    </html>
"""
    return HttpResponse(text)
