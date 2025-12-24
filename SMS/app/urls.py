from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path('', views.home, name="hello"),
    path('base/',views.base, name="base"),
    
]
