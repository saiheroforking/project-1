from django.shortcuts import render, redirect,get_object_or_404
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

def update_details(request, pk):
    student = get_object_or_404(Student, id=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('app:Show')
    else:
        form = StudentForm(instance=student)

    return render(request, 'update_details.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('app:Show')
