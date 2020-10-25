from django.db import models

# Create your models here.
class Carousel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='carousel-image')

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos')
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    subject = models.CharField(max_length=100)
    message = models.TextField()


    def __str__(self):
        return self.name +" "+self.phone
    

    