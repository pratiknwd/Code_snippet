from django.db import models
from django import forms

# Create your models here.

class SavedData(models.Model):
    title = models.CharField(max_length=250)
    code = models.TextField()
    
    #Converting it to str output for Console Preview.
    def __str__(self):
        return f"This {self.id} has {self.title}: {self.code}"