from django.urls import path
from.import views

#urlpatterns =[path('',views.rango_list),
urlpatterns =[
   
    path('', views.home,name ='home'),
    path('about/',views.about, name="about"),
    path('Log/',  views.Log, name="Log"),
    

]
