"""
Echo Urls
"""
from django.urls import path
from . import views
app_name="echo"

urlpatterns = [
    path('', views.index , name="index"),
    path('api/', views.api , name="api"),
]
