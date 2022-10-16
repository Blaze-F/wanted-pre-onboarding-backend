from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    register = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
class Job_opening(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    wanted = models.CharField(max_length=200)
    reward = models.IntegerField()
    content = models.TextField()
    stack = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

class Applicate(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    job_opening = models.ForeignKey(Job_opening, on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)