from django.urls import path
from .views import *

urlpatterns = [
    path('all-sem/', all_semester.as_view(), name="student_all_semester")
]