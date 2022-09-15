from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from IssueApp.models import Issue
from IssueApp.serializers import IssueAppSerializer
from rest_framework import status;

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def IssueApi(request,id=0):
   
    #Getting a list of all issues and subsequent assignee, reporter.
    if request.method=='GET':
        issues = Issue.objects.all()
        issues_serializer=IssueAppSerializer(issues,many=True)
        return JsonResponse(issues_serializer.data,safe=False)

    #Create an issue under a project by using project id or project name -> Project Id Passed As an Argument of Foreign Key    
    elif request.method=='POST':
        issues_data=JSONParser().parse(request)
        issues_serializer=IssueAppSerializer(data=issues_data)
        if issues_serializer.is_valid():
            issues_serializer.save()
            return JsonResponse("Issues Added Successfully",safe=False)
        return JsonResponse(issues_serializer.errors,safe=False)

    #Update a Issue but this will make ensure that reporter would not be updated
    elif request.method =='PUT':
     issues_data=JSONParser().parse(request)
     issue= Issue.objects.get(id=issues_data['id'])
     issue_serializer=IssueAppSerializer(issue,data=issues_data)
    if issue_serializer.is_valid():
       issue_serializer.save()
       return JsonResponse("Issue Updated Successfully",safe=False)
    return JsonResponse(issue_serializer.errors,status=status.HTTP_400_BAD_REQUEST);   


#Gets An Issue Details With Id As An Parameter
#Follow This Get Request Format : http://127.0.0.1:8000/issue/?id=10
@csrf_exempt     
def IssueApiIdParam(request):
     if request.method=='GET':
        id = request.GET['id']
        issues_filter = Issue.objects.filter(id=id)
        issues_serializer=IssueAppSerializer(issues_filter,many=True)
        return JsonResponse(issues_serializer.data,safe=False)