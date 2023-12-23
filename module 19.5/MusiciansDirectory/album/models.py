from django.db import models
from musician.models import Musician
# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'),]
    rating = models.IntegerField(choices=CHOICES)

    def __str__(self):
        return self.album_name