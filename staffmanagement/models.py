from django.db import models
from sign_up.models import User
# Create your models here.


class Staff(models.Model):
    name=models.CharField(max_length=300)
    subject=models.CharField(max_length=300)
    password=models.CharField(max_length=300)
    active = models.BooleanField(default=True)  
    admin = models.ForeignKey(User, on_delete=models.CASCADE) # boss to manage the site
    attendance = models.PositiveIntegerField()
    salary = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    