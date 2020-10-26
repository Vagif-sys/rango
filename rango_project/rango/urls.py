from django.urls import path
from.import views

#urlpatterns =[path('',views.rango_list),
urlpatterns =[
   
    path('', views.home,name ='home'),
    

]
