from django.db import models


class Team(models.Model):
    client1 = models.CharField(max_length=50, default="pending")
    name = models.CharField(max_length=50, default="pending")
    title = models.CharField(max_length=50, default="pending")
    image = models.ImageField(upload_to='images/', default="pending")

# Create your models here.


class slider(models.Model):
    slinder_name = models.CharField(max_length=50, default="pending")
    slinder_desc = models.CharField(max_length=50, default="pending")
    img = models.ImageField(upload_to='images/')