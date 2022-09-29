from django.db import models

# Create your models here.

class Student(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=60)
    dob=models.DateField()
    marks=models.IntegerField()
    email=models.EmailField()
    phone_number=models.IntegerField()
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.name