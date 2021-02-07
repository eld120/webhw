from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("CSS/", views.CSS, name="CSS"),
    path("Django/", views.Django, name="Django"),
    path("Git/", views.Git, name="Git"),
    path("HTML/", views.HTML, name="HTML"),
    path("Python/", views.Python, name="Python"),
    path('search/', views.search, name='search'),
    path('newpage/', views.newpage, name='newpage'),
]
