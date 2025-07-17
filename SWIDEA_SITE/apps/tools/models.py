from django.db import models

# Create your models here.
class Tool(models.Model):
    name = models.CharField("툴이름",max_length=20,unique=True)
    kind = models.CharField("툴타입",max_length=50)
    content = models.TextField("툴설명")

    def __str__(self):
        return self.name
