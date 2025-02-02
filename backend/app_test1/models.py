from django.db import models

# Create your models here.


class Writer(models.Model):
    firstname = models.CharField(max_length=180)
    lastname = models.CharField(max_length=180)
    email = models.EmailField()
    country = models.CharField(max_length=180)

    def __str__(self):
        return f"{self.firstname} - {self.lastname}"
