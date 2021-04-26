from django.db import models
from datetime import date

STATE_CHOICE=(
  ('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh' , 'Arunachal Pradesh'),
('Assam' , 'Assam'),
('Bihar' , 'Bihar'),
('Chhatisgarh' , 'Chhattisgarh'),
('Goa' , 'Goa'),
('Gujrat' , 'Gujarat'),
('Haryana' , 'Haryana'),
('Himachal Pradesh' , 'Himachal Pradesh'),
('Janmu and Kashmir', 'Jammu and Kashmir'),
('Jharkhand', 'Jharkhand'),
('Karnataka' , 'Karnataka'),
('Kerala' , 'Kerala'),
('Madhya Pradesh' , 'Madhya Pradesh'),
('Maharashtra' , 'Maharashtra'),
('MN' , 'Manipur')
)

# Create your models here.
class Resume(models.Model):
  name=models.CharField(max_length=100)
  dob=models.DateField(auto_now=False, auto_now_add=False)
  gender=models.CharField(max_length=100)
  locality=models.CharField(max_length=100)
  city=models.CharField(max_length=100)
  pin=models.PositiveIntegerField()
  state=models.CharField(choices=STATE_CHOICE,max_length=50)
  email=models.EmailField()
  mobile=models.PositiveIntegerField()
  job_city=models.CharField(max_length=100)
  profile_image=models.ImageField(upload_to='profileimg', blank=True)
  my_file=models.FileField(upload_to='doc', blank=True)
  DisplayFields=['id','name','dob','age','gender','locality','city','pin','state','email','mobile','job_city','profile_image','my_file']
  searchableFields=['name','gender']
  FilterFields=['state']
  @property
  def age(self):
    if(self.dob!=None):
      age=date.today().year - self.dob.year
      return age
