from django.urls import path, re_path, include
from . import views


urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.login_user, name="logout"),
    path('register_user', views.register_user, name="register_user"),
    ]
