from django.db import models

class MyWatchlist(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.CharField(max_length=225)
    watched = models.BooleanField()
    rating = models.IntegerField()
    review = models.TextField()