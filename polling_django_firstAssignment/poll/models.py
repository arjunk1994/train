from django.db import models

class pollstr(models.Model):
    order = models.CharField(default="only", max_length=50)
    votes1=models.CharField(default ="0", max_length=50)
    votes2=models.CharField(default ="0", max_length=50)
    votes3=models.CharField(default ="0", max_length=50)
    votes4=models.CharField(default ="0", max_length=50)
    
    
    def __str__(self):
        return (self.order)

