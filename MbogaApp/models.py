from django.db import models


# Create your models here.
class Username(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    color = models.CharField(max_length=100, default="white")

    def __str__(self):
        return self.name


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.title
