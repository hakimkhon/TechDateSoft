from turtle import home
from django.contrib import admin
from django.urls import path, include
from students.views import home



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('leads/', include('students.urls', namespace="leads"))
]
