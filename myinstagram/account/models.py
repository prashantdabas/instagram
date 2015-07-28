from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=128,unique=True)
    code=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.code

class State(models.Model):
    name = models.CharField(max_length = 128,unique = True)
    country = models.ForeignKey(Country)
    code=models.CharField(max_length = 10)
    def __str__(self):
        return self.country.code +">" +self.name
    
class City(models.Model):
    state = models.ForeignKey(State)
    name = models.CharField(max_length = 128,unique = True)
    def __str__(self):
        return self.state.county.code + ">" +self.state.code + ">" + self.name
    
class Profile(models.Model):
    account = models.OneToOneField(User,primary_key = True)
    profile_pic = models.ImageField(upload_to = 'profile_pic/',blank=True)
    following=models.ManyToManyField(User,related_name='followers')
    city = models.ForeignKey(City,blank=True,null=True)
    street_address = models.CharField(max_length=256,blank=True,null=True)