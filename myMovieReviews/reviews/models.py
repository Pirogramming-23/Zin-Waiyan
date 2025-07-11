from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=32)
    year = models.CharField(max_length=5)
    genre = models.CharField(max_length=32)
    review_star = models.FloatField()
    director = models.CharField(max_length=32)
    actors = models.CharField(max_length=32)
    running_time = models.PositiveIntegerField()
    content = models.TextField()