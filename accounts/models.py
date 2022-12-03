
from django.db import models

# Create your models here.

class library_db(models.Model):
    username = models.CharField(max_length=100)
    libraryId = models.CharField(max_length=100)
    bookTitle = models.CharField(max_length=200)
    dateOut = models.DateField()
    dueDate = models.DateField()
    due = models.IntegerField()
