from django.urls import path
from . import views 
urlpatterns = [

    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('base/',views.base,name='base'),
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('common/',views.common,name='common'),

]



