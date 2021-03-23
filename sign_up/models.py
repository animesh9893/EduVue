from django.db import models

# Create your models here.
class User(models.Model):
    user_name =  models.CharField(max_length=30)  
    password =  models.CharField(max_length=30)  
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_name
        
    def get_absolute_url(self):
        return "/home/%i" % self.id
    