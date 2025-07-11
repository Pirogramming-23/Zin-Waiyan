from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=32)
    year = models.CharField(max_length=5)
    GENRE_CHOICES = [
        ("action", "액션"),
        ("drama", "드라마"),
        ("comedy", "코미디"),
        ("sf", "SF"),
        ("thriller", "스릴러"),
        ("romance", "로맨스"),
        ("animation", "애니메이션"),
        ("documentary", "다큐멘터리"),
        ("fantasy","판타지")
    ]
    genre = models.CharField(max_length=32,choices=GENRE_CHOICES)
    review_star = models.FloatField()
    director = models.CharField(max_length=32)
    actors = models.CharField(max_length=32)
    running_time = models.PositiveIntegerField()
    review_text = models.TextField()