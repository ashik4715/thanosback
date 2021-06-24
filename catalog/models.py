from django.db import models

# Create your models here.
class Catalog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.CharField(max_length=1000)
    background_image = models.CharField(max_length=1000)
    genre = models.CharField(max_length=1000)
    bio = models.TextField(max_length=2500)
    release_date = models.DateField('date released')
    review = models.IntegerField(default=[0])    

    def __str__(self):
        return self.title