from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=32)
    year = models.CharField(max_length=5)
    GENRE_CHOICES = [
        ("Action", "액션"),
        ("Drama", "드라마"),
        ("Comedy", "코미디"),
        ("SF", "SF"),
        ("Thriller", "스릴러"),
        ("Romance", "로맨스"),
        ("Animation", "애니메이션"),
        ("Documentary", "다큐멘터리"),
        ("Fantasy","판타지"),
    ]
    genre = models.CharField(max_length=32,choices=GENRE_CHOICES)
    review_star = models.FloatField()
    director = models.CharField(max_length=32)
    actors = models.CharField(max_length=32)
    running_time = models.PositiveIntegerField()
    review_text = models.TextField()