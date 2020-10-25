from django.urls import path
from.views import Home,About

#urlpatterns =[path('',views.rango_list),
urlpatterns =[
    path('about/', About.as_view(),name ='about'),
    path('', Home.as_view(),name ='home'),
    

]
