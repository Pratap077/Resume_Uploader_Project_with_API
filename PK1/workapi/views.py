from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from rest_framework import viewsets
# Create your views here.
class Bookapi(APIView):
  serializer_class=BookSerilizers
  def get(self,request):
    allbook = Book.objects.all().values()
    return Response({"Message":"List of book","Book":allbook})

  def post(self,request):
    serializer_obj=BookSerilizers(data=request.data)
    print(serializer_obj)
    if(serializer_obj.is_valid()):
      Book.objects.create(id=serializer_obj.data.get("id"),
                        title=serializer_obj.data.get("title"),
                        author=serializer_obj.data.get("author"),)
    book = Book.objects.all().filter(id=request.data['id']).values()
    print(book)
    return Response({'Messege':'New book added','Book':book})
      
class StudentViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer