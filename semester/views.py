from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class all_semester(APIView):
    def get(self, request):
        semesterList = {'1425647852': {'1':'1st Semester', '2':'2nd Semester', '3':'3rd Semester', '4':'4th Semester', '5':'5th Semester', '6':'6th Semester', '7':'7th Semester', '8':'8th Semester'}, 
            '1425621432': {'1':'1st Semester', '2':'2nd Semester', '3':'3rd Semester', '4':'4th Semester', '5':'5th Semester', '6':'6th Semester'}
        }
        if 'student_roll' not in request.GET:
            resp = {
                'student_id' : 'null',
                'message': "student_roll not given"
            }
            return Response(resp, status=400)
        if request.GET['student_roll'] in semesterList.keys():
            resp = {
                'student_id' : request.GET['student_roll'],
                'message': "semester_foind",
                'semesters': semesterList[request.GET['student_roll']]
            }
        else:
            resp = {
                'student_id' : request.GET['student_roll'],
                'message': "Semester not found",
            }
            return Response(resp, status=400)
        return Response(resp, status=200)