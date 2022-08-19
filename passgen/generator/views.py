from operator import imod
from django.shortcuts import render
from django.http import HttpResponse
import random
import datetime


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    y = datetime.datetime.now()
    return render(request, 'generator/about.html', {'year': y.year})


def password(request):
    length = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    lowercase = request.GET.get('lowercase')
    numbers = request.GET.get('numbers')
    symbols = request.GET.get('symbols')

    chars = list('')
    if uppercase:
        chars.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if lowercase:
        chars.extend('abcdefghijklmnopqrstuvwxyz')
    if numbers:
        chars.extend('0123456789')
    if symbols:
        chars.extend('!@#$%^&*()_+=-')

    finalpass = ''
    for i in range(length):
        finalpass += random.choice(chars)

    return render(request, 'generator/password.html', {'password': finalpass})
