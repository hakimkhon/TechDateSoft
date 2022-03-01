from turtle import home
from django.contrib import admin
from django.urls import path, include
from students.views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view()),
    path('leads/', include('students.urls', namespace="leads"))
]
