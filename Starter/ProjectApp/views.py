from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ProjectApp.models import Project
from ProjectApp.serializers import ProjectAppSerializer


# Create your views here.
@csrf_exempt
#Retrive All The Project Details
def projectApi(request,id=0):
 if request.method =='GET':
    projects = Project.objects.all()
    projects_serializer=ProjectAppSerializer(projects,many=True)
    return JsonResponse(projects_serializer.data,safe=False)

#Create a project.
 elif request.method =='POST':
    project_data=JSONParser().parse(request)
    project_serializer=ProjectAppSerializer(data=project_data)
    if project_serializer.is_valid():
       project_serializer.save()
       return JsonResponse("Project Added Successfully",safe=False)
    return JsonResponse("Failed to Add Project",safe=False)

#Update a Project
 elif request.method =='PUT':
    project_data=JSONParser().parse(request)
    project= Project.objects.get(id=project_data['id'])
    project_serializer=ProjectAppSerializer(project,data=project_data)
    if project_serializer.is_valid():
       project_serializer.save()
       return JsonResponse("Project Updated Successfully",safe=False)
    return JsonResponse("Failed to Update the Project")

#Delete a Project By Id As a Parameter
#Follow This Delete Request Format : http://127.0.0.1:8000/project/2
 elif request.method =='DELETE':
    project= Project.objects.get(id=id)
    project.delete()
    return JsonResponse("Project Deleted Successfully",safe=False)  

#Gets An Project Details With Id As An Parameter
#Follow This Get Request Format : http://127.0.0.1:8000/project/?id=10
@csrf_exempt     
def ProjectApiIdParam(request):
     if request.method=='GET':
        id = request.GET['id']
        project_filter = Project.objects.filter(id=id)
        project_serializer=ProjectAppSerializer(project_filter,many=True)
        return JsonResponse(project_serializer.data,safe=False)