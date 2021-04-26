from rest_framework import serializers
from .models import Book,Student

class BookSerilizers(serializers.Serializer):
  id=serializers.IntegerField(label="Enter Book Id")
  title=serializers.CharField(label="Enter Book Name")
  author=serializers.CharField(label="Enter Book Author")

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student  
    fields = "__all__"