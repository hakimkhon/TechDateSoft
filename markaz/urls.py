from django.contrib import admin
# urls.py
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('students.urls', namespace="leads"))
]
