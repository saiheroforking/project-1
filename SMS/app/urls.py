from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("list/", views.flavor_list, name="flavor_list"),
    path("update/<int:id>/", views.update_flavor, name="update_flavor"),
    path("delete/<int:id>/", views.delete_flavor, name="delete_flavor"),
    

]
