from django.shortcuts import render
from .models import Student
from django.db.models import Q

# Create your views here.

def home_view(request):
    student=Student.objects.filter(~Q(phone_number__range=(250,10000)))
    print("--------")
    print(student.count())
    print("--------")

    return render(request,'testapp/home.html',{'student':student})

