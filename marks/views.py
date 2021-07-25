from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class all_marks(APIView):
    def get(self, request):        
        marks = {
            '1425647852':
            {
                '1': {
                    '1st internal':
                    {
                        'English': 10
                    },
                    '2nd internal':
                    {
                        'Math': 10
                    }
                }
            },
            '1425621432':
            {
                '1': {
                    '1st internal':
                    {
                        'Computer': 10
                    },
                    '2nd internal':
                    {
                        'Application': 9
                    }
                }
            }
        }
        
        if request.GET['student_roll'] in marks:
            if request.GET['semester'] in marks[request.GET['student_roll']]:
                resp = marks[request.GET['student_roll']][request.GET['semester']]
                return Response(resp, status=200)

        # print (marks[request.GET['student_roll']][request.GET['semester']])
        # return Response(marks, status=200)