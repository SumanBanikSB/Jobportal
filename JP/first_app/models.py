from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Company Model..
class Company(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    position = models.CharField(max_length=200, null = True)
    description = models.CharField(max_length=2000, null=False)
    salary = models.IntegerField(null = True)
    experience = models.IntegerField(null = True)
    location = models.CharField(max_length=2000, null = True)

    def __str__(self):
        return self.name

class Candidates(models.Model):
    category = (
        ('M', 'male'),
        ('F','female'),
        ('Other','Other'),
    )
    name = models.CharField(max_length=200, null = True)
    dob = models.DateField(null = True,auto_now_add=True)
    gender = models.CharField(max_length = 10, choices=category)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    resume = models.FileField()
    company = models.ManyToManyField(Company, blank = True)

    def __str__(self):
        return self.name


