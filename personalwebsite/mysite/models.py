from django.db import models

# Create your models here.
class contact(models.Model):
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message= models.TextField()

    def __str__(self):
        return self.email



class quotes(models.Model):
    authorname=models.CharField(max_length=50)
    quote= models.TextField()

    def __str__(self):
        return self.authorname



class sayings(models.Model):
    name=models.CharField(max_length=50)
    saying= models.TextField()

    def __str__(self):
        return self.name



