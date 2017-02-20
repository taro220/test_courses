from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    return render(request, "courseList/index.html")

def add(request):
    if request.method == "POST":
        Course.objects.create(name = request.POST['name'], description = request.POST['description'])
        print Course.objects.all()
    return redirect('/')
