from django.urls import path
from . import views

urlpatterns= [
    path('',views.index, name='index'),
    path('search/',views.search, name='search'),
    # pathv('/dashboard', views.form, name='dashboard'),
] 