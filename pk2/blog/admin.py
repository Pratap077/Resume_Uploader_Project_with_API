from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Block)
class BlockModelAdmin(admin.ModelAdmin):
  list_display=('id','name','email','mobile','city')
@admin.register(StudentBlock)
class StudentModelAdmin(admin.ModelAdmin):
  list_display=('id','first_name','last_name','dob')  
 
"""from django.apps import apps
from .models import *

models=apps.get_models()
for model in models:
  admin.site.register(model)"""
 
