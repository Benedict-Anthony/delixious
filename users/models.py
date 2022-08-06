from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    customer = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    contact = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Rider(models.Model):
    gender = [
        ("male", "male"),
        ("female","female")
        ]
    
    status = [
        ("married", "married"),
        ("single","single")
        ]
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.EmailField(max_length=50)
    image = models.ImageField(upload_to="images", default="")
    address = models.TextField(max_length=100, default="")
    status = models.CharField(max_length=15, choices=status, default="single")
    gender = models.CharField(max_length=15, choices=gender, default="male")
    own_a_bike = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Blog(models.Model):
    title = models.CharField(max_length=20)
    post = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    
class Review(models.Model): 
    name = models.CharField(max_length=50)
    review = models.TextField(max_length=150)
    date = models.DateField(auto_now_add=True)

    