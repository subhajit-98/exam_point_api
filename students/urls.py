from django.urls import path
from .views import *

urlpatterns = [
    path('check/', check_student.as_view(), name="check_student")
]