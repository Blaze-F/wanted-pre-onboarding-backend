from django.db import models

# Create your models here.

class Job_opening(models.Model):
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    stack = models.TextField()
    create_date = models.DateTimeField()


class Applicate(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()