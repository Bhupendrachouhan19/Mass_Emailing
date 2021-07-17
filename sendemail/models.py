from django.db import models
# Create your models here.

class Newsletter(models.Model):
    email = models.EmailField(max_length=50) #Here email is the database entry.

    def __str__(self):
        return self.email

#Models in python are a class which represent a table in a database