from re import template
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
# from django.views.generic import TemplateView
from . import models
from .forms import *

# class HomeView(TemplateView):
#     template_name = ("home.html")

def home(request):
    return render(request, "home.html")

def student_lists(request):
    talaba = models.Student.objects.all
    context = {
        "leads": talaba
    }
    return render(request, "student/student_lists.html", context)

def student_details(request, pk):
    pktalaba = get_object_or_404(models.Student, id = pk)
    context = {
        "lead": pktalaba
    }
    return render(request, "student/student_details.html", context)

def student_create(request):
    form = StudentModelForm()
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "forms": form
    }
    return render(request, "student/student_create.html", context)

def student_update(request, pk):
    talaba = models.Student.objects.get(id = pk)
    form = StudentModelForm(instance = talaba)
    if request.method == "POST":
        form = StudentModelForm(request.POST, instance = talaba)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": talaba
    }
    return render(request, "student/student_update.html", context)

def student_delete(request, pk):
    talaba = models.Student.objects.get(id = pk)
    talaba.delete()
    return redirect("/leads")