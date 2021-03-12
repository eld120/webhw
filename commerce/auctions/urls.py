from django.urls import path
from .views import IndexView, ListingCreate, ListingDetail
from . import views

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path('lcr/', ListingCreate.as_view(), name='listing_create'),
    path('detail/<slug:slug>', ListingDetail.as_view(), name='listing_detail'),
    #path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register")
]
