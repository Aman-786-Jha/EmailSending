from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(unique=True,blank=False,null=False)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    
    age= models.PositiveIntegerField()
    phone_number = models.PositiveIntegerField(max_length=10,unique =True, blank=False,null=False)

    def __str__(self):
        return self.name 