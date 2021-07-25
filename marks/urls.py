from django.urls import path
from .views import *

urlpatterns = [
    path('all-marks/', all_marks.as_view(), name="student_all_marks")
]