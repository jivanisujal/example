from django.db import models

# Create your models here.
class Students (models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    contact = models.BigIntegerField()

    def __str__(self):
        return self.name