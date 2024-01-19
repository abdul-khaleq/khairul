from django.db import models
from service_app.models import ServiceModel
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class EmployeeModel(models.Model):
    company_name = models.CharField(max_length = 100,blank = True, null = True)
    position = models.IntegerField(blank = True, null = True)
    title = models.CharField(max_length=255,blank = True, null = True)
    description = models.TextField(blank = True, null = True)
    requirements = models.TextField(blank = True, null = True)
    location = models.CharField(max_length=255, blank = True, null = True)
    date_posted = models.DateTimeField(default=timezone.now, blank = True, null = True)
    salary = models.IntegerField()
    service = models.ForeignKey(ServiceModel, on_delete = models.CASCADE, blank = True, null = True)
    image = models.ImageField(upload_to= 'job_app/media/uploads/')
    def __str__(self):
        return self.company_name
    
class Job_seeker(models.Model):
    Cv=models.ImageField(upload_to='cv', blank=True, null=True)
    employee=models.ForeignKey(EmployeeModel,on_delete= models.CASCADE)
    user=models.ForeignKey(User,on_delete= models.CASCADE)
    def __str__(self) -> str:
        return f'{self.user}'

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    employee = models.ForeignKey(EmployeeModel, on_delete = models.CASCADE, related_name = 'comments')

    def __str__(self) -> str:
        return f'comment by {self.name}'