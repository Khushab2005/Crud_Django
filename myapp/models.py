from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False)
    email = models.EmailField(unique=True,blank=False,null=False)
    city = models.TextField()
    phone = models.CharField(max_length=15,blank=False,null=False)
    
    def __str__(self):
        return self.name
    
    
    