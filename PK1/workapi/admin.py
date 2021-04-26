from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Book)
class LibraryModelAdmin(admin.ModelAdmin):
  list_display=('id','title','author')
  
@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
  list_display=('id','first_name','last_name','dob','age')
  search_fields=Student.serachableFields
  