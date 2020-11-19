from django.shortcuts import  render, get_object_or_404,redirect
from.models import Customer
from django.utils import timezone
from.forms import CustForm

def home(request):

    return render(request, "rango/home.html",{})

def about(request):
    products = Product.objects.all()
    return render(request,'rango/about.html',{'products': products})

def Log(request):
    if request.method == 'POST':
       form = CustForm(request.POST)
       if form.is_valid():
           post = form.save()
           post.title = request.user
           post.date_created =timezone.now()
           post.save()
           return redirect('about')
    else:
         form = CustForm()
    return render(request, "Log.html",{'form':form})

