from django.db import models

# Create your models here.
class Block(models.Model):
  id=models.IntegerField(primary_key=True)
  name=models.CharField(max_length=50)
  email=models.EmailField(max_length=50)
  mobile=models.IntegerField()
  city=models.CharField(max_length=50)

class StudentBlock(models.Model):
  id=models.IntegerField(primary_key=True)
  first_name=models.CharField(max_length=50)  
  last_name=models.CharField(max_length=50,null=True,blank=True)
  dob=models.DateField(null=True,blank=True)
 
 
