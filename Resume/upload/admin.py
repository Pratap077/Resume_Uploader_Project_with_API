from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Resume)
@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
  list_display=Resume.DisplayFields
  """list_display=('id','name','dob','gender','locality','city','pin','state','email','mobile','job_city','profile_image','my_file')"""
  search_fields=Resume.searchableFields
  list_filter=Resume.FilterFields
  