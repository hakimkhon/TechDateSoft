from django.urls import path
# ulrs.py in application
from .views import *

app_name = "leads"

urlpatterns = [
    path('', student_lists, name="student_lists"),
    path('<int:pk>/', student_details, name="student_details"),
    path('<int:pk>/update/', student_update, name="student_update"),
    path('<int:pk>/delete/', student_delete, name="student_delete"),
    path('student_create/', student_create, name="student_create")
]