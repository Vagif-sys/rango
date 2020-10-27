from django.shortcuts import render
from.models import Question
from django.utils import timezone

def home(request):
    posts = Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, "rango/home.html",{'posts':posts})

