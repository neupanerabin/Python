from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),        # access to signup.html page
    path('signin', views.signin, name="signin"),        # access to signin.html page
    path('signout', views.signout, name="signout"),     # access to signout.html page
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]
