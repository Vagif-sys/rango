from django.shortcuts import get_object_or_404, render
from.models import Question
from django.utils import timezone

def home(request):
    posts = Question.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, "rango/home.html",{'posts':posts})

def about(request,title):
    return render(request,'rango/about.html',{'title': title})

