from django.urls import path
from .views import *

app_name = "leads"

urlpatterns = [
    path('', StudentListView.as_view(), name="student_lists"),
    path('<int:pk>/', StudentDetailView.as_view(), name="student_details"),
    path('<int:pk>/update', StudentUpdateView.as_view(), name="student_update"),
    path('<int:pk>/delete', StudentCDeleteView.as_view(), name="student_delete"),
    path('student_create/', StudentCreateView.as_view(), name="student_create")
]