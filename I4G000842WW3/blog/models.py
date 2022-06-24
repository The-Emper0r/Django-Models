from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.utils import timezone



class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_Date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
