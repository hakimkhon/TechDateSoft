from django.shortcuts import render, redirect
from . import models
from .forms import *
from django.shortcuts import get_object_or_404

import students

def student_lists(request):
    talaba = models.Student.objects.all
    context = {
        "leads": talaba
    }
    return render(request, "student_lists.html", context)

def student_details(request, pk):
    pktalaba = get_object_or_404(models.Student, id = pk)
    context = {
        "lead": pktalaba
    }
    return render(request, "student_details.html", context)

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
    return render(request, "student_create.html", context)

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
    return render(request, "student_update.html", context)

def student_delete(request, pk):
    talaba = models.Student.objects.get(id = pk)
    talaba.delete()
    return redirect("/leads")