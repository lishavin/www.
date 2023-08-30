from django import views
from django.urls import path, include
from .views import signup,login,logout,home,edit

urlpatterns = [
    path('signup/', signup, name= 'signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', edit, name='edit'),
    path('', home, name='home'),

]
