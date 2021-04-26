from upload.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
 class Meta:
  model = Resume
  fields = ['id','name','dob','gender','locality','city','pin','state','email','mobile','job_city','profile_image','my_file']