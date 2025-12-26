from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app:success")
    else:
        form = StudentForm()

    return render(request, "home_page.html", {"form": form})


def success(request):
    return render(request, "success.html")


def Show(request):
    show_details = Student.objects.all()
    return render(request,"Show_Details.html",{"Show_details":show_details})

