from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    context = {}
    return render(request, 'main/home.html', context)
