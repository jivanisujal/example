from django.shortcuts import render
from apidemo.models import *
from django.http import HttpResponse,JsonResponse
from django.core.serializers import serialize
# Create your views here.

def get_students(request):
    data = list(Students.objects.values())
    print(data)
    return JsonResponse({"students":data})
def add_student(request):
    if 'name' in request.GET:
        name = request.GET['name']
        email = request.GET['email']
        contact = request.GET['contact']
        obj = Students(
            name = name,
            email = email,
            contact = contact,
        )
        obj.save()
        print(obj)
        jsonData = serialize("json",[obj])
    return JsonResponse({"student":jsonData,'status':1})