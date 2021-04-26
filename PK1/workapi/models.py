from django.db import models
from datetime import date

# Create your models here.
class Book(models.Model):
  id=models.IntegerField(primary_key=True)
  title=models.CharField(max_length=200)
  author=models.CharField(max_length=200)

class Student(models.Model):
  id=models.IntegerField(primary_key=True)
  first_name=models.CharField(max_length=200)
  last_name=models.CharField(max_length=200,null=True,blank=True)
  dob=models.DateField(null=True,blank=True)
  serachableFields=['first_name','last_name']
  
  @property
  def age(self):
    if(self.dob!=None):
      age=date.today().year - self.dob.year
      return age
