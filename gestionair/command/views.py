# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect



def home(request):
    text = """<h1>Bienvenue sur le Gestion'air !</h1>"""
    return HttpResponse(text)

def temps_attente(request):
    return redirect("url")

def resultat(request):
    return redirect("url")

def compte_a_rebours(request):
    return redirect("url")

def temps_attente_html(request):
    return redirect("url")

def resultat_html(request):
    return redirect("url")

def compte_a_rebours(request):
    return redirect("url")