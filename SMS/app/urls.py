from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.student_form, name="create"),
    path("success/", views.success, name="success"),
    path("Show/",views.Show,name="Show"),
]   
