from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from webapp1.models import classcast_student_info
import json


class phonenumber(APIView):
        def post(self, request, format = None):
                data1 = request.data
                #data2 = json.loads(data1)
                student_name=[]
                student_phone=[]
                for items in data1['number']:
                        obj = classcast_student_info.objects.get(phone_number = items)
                        student_name.append(obj.student_id)
                        student_phone.append(items)
                
                result=dict(zip(student_name,student_phone))
                return HttpResponse(json.dumps(result))

