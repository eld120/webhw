from django.urls import path, re_path

from . import views
#app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.entry, name='entry'),
    
    path('search/', views.search, name='search'),
    path('newpage/', views.newpage, name='newpage'),
    path('edit/<str:title>', views.edit, name='edit')
    #re_path(r'^edit/(?P<title>)/$', views.edit, name='edit')
]
