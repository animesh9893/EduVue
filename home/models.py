from django.db import models

# Create your models here.
class WhyEduVueText(models.Model):
    head_text=models.CharField(max_length=300)  
    abbrivationtext= models.CharField(max_length=500)
    display = models.BooleanField()  

    def __str__(self):
        return self.head_text
    