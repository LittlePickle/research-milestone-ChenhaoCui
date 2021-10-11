from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'registration.html')