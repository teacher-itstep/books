from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.CharField(max_length=120)
    year = models.IntegerField()


    def __str__(self):
        return self.title
