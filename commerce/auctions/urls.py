from django.urls import path
from .views import IndexView
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    #path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
