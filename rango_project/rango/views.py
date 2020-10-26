from django.shortcuts import render
from.models import Question

def home(request):
    return render(request, "rango/home.html",{})

