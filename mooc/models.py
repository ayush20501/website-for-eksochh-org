from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=10)
    Email = models.EmailField()
    Insta = models.CharField(max_length=10)
    Comments = models.CharField(max_length=200)

    def __str__(self):
        return self.Name

class Confession(models.Model):
    Confess = models.CharField(max_length=500)

    c = "confession"
    def __str__(self):
        return self.c


class Image(models.Model):
    image = models.URLField(default="")
