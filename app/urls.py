from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
    path("", views.student_form, name="create"),
    path("success/", views.success, name="success"),
    path("Show/",views.Show,name="Show"),
    path('update/<int:pk>/', views.update_details, name='update_details'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]