from django.urls import path
from.import views


urlpatterns =[
   
    path('', views.home,name ='home'),
    path('about/',views.about, name="about"),
    path('creatOrder/',  views.creatOrder, name="creatOrder"),
    path('customer/<str:pk_test>/',  views.customer, name="customer"),
    path('updateOrder/<str:pk>/',  views.updateOrder, name="updateOrder"),
    path('deleteOrder/<str:pk>/',  views.deleteOrder, name="deleteOrder"),
   

]
