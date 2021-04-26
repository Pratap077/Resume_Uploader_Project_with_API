from django.shortcuts import render
from .models import Block, StudentBlock
from .serializers import BlockData, StudentSerilizer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.
def detail_view(request,pk):
  blu=Block.objects.get(id=pk)
  serializer=BlockData(blu)
  return JsonResponse(serializer.data)

def list_view(request):
  blu=Block.objects.all()
  serializer=BlockData(blu,many=True)
  return JsonResponse(serializer.data,safe=False)  

class project_api(APIView):
  serializer_class=BlockData
  def get(self,request):
    list_data = Block.objects.all().values()
    return Response({list_data})
  def post(self,request):
    serializer_obj=BlockData(data=request.data)
    if(serializer_obj.is_valid()):
      Block.objects.create(id=serializer_obj.data.get('id'),
      name=serializer_obj.data.get('name'),
      email=serializer_obj.data.get('email'),
      mobile=serializer_obj.data.get('mobile'),
      city=serializer_obj.data.get('city'))

      data=Block.objects.all().filter(id=request.data['id']).values()
      return Response({data})

class Student_blockViewSet(viewsets.ModelViewSet):
  queryset=StudentBlock.objects.all()
  serializer_class = StudentSerilizer 
  


