from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "input_box",
                "placeholder": "Enter student name"
            }),

            "Email": forms.EmailInput(attrs={
                "class": "input_box",
                "placeholder": "Enter the email Address"
            }),

            "phone_no": forms.NumberInput(attrs={
                "class": "input_box",
                "placeholder": "Enter Phone number"
            }),

            "roll_no": forms.NumberInput(attrs={
                "class": "input_box",
                "placeholder": "Enter the Roll Number"
            }),

            "Branch": forms.TextInput(attrs={
                "class": "input_box",
                "placeholder": "Enter the Branch"
            }),

            "course": forms.TextInput(attrs={
                "class": "input_box",
                "placeholder": "Enter the Course"
            }),
        }
