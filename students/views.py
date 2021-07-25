from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class check_student(APIView):
    def get(self, request):
        existing_students = ['1425647852', '1425621432']
        if 'student_roll' not in request.GET:
            resp = {
                'student_id' : 'null',
                'message': "student_roll not given"
            }
            return Response(resp, status=400)
        if request.GET['student_roll'] in existing_students:
            resp = {
                'status': 'success',
                'student_id' : request.GET['student_roll'],
                'message': "student_found"
            }
        else:
            resp = {
                'status': 'error',
                'student_id' : request.GET['student_roll'],
                'message': "Student not found",
            }
            return Response(resp, status=400)
        return Response(resp, status=200)