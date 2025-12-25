from django.db import models
class Student(models.Model):
    name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100, default="")
    phone_no = models.IntegerField(default=0)
    roll_no = models.CharField(max_length=10, default="")
    Branch = models.CharField(max_length=20, default="")
    course = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name
