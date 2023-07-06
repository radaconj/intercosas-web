from django.db import models
import datetime


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='innit/images')
    date = models.DateField(datetime.date.today())
    autor = models.CharField(max_length=100)
