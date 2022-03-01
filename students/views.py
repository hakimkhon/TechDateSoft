from multiprocessing import context
from re import template
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .forms import *

class HomePage(TemplateView):
    template_name = ("home.html")

class StudentListView(ListView):
    template_name = "student/student_lists.html"
    queryset = models.Student.objects.all()
    context_object_name = "leads"

class StudentDetailView(DetailView):
    template_name = "student/student_details.html"
    queryset = models.Student.objects.all()
    context_object_name = "lead"

class StudentCreateView(CreateView):
    template_name = "student/student_create.html"
    form_class = StudentModelForm

    def get_success_url(self):
        return reverse('leads:student_lists')

class StudentUpdateView(UpdateView):
    template_name = "student/student_update.html"
    form_class = StudentModelForm
    queryset = models.Student.objects.all()

    def get_success_url(self):
        return reverse('leads:student_lists')

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

class StudentCDeleteView(DeleteView):
    template_name = "student/student_delate.html"
    form_class = StudentModelForm
    queryset = models.Student.objects.all()

    def get_success_url(self):
        return reverse('leads:student_lists')

# def student_delete(request, pk):
#     talaba = models.Student.objects.get(id = pk)
#     talaba.delete()
#     return redirect("/leads")