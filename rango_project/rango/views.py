from django.shortcuts import  render, get_object_or_404
from.models import Question
from django.utils import timezone
from.forms import QuestForm

def home(request):
    posts = Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, "rango/home.html",{'posts':posts})

def about(request):
    return render(request,'rango/about.html')

def Log(request):
    form = QuestForm()
    return render(request, "Log.html",{'form':form})

