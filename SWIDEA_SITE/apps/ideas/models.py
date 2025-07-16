#apps.ideas.models.py
from django.db import models
from apps.tools.models import Tool
from django.utils import timezone

# Create your models here.
class Idea(models.Model):
    # image, title, interest, devtool, content, created_at, updated_at, favorite
    title = models.CharField('제목',max_length=20)
    image = models.ImageField('이미지',blank=True,upload_to='ideas/%Y%m%d')
    interest = models.PositiveIntegerField('관심도',default=0)
    content = models.TextField('설명')

    devtool = models.ForeignKey(Tool,verbose_name='개발툴',on_delete=models.CASCADE)
    
    created_at = models.DateTimeField("작성일",auto_now_add=True)
    updated_at = models.DateTimeField('수정일', null=True, blank=True)

    def __str__(self):
        return self.title

    # record the updated time only when editing, not when first creating
    def save(self, *args, **kwargs):
        if self.pk:  
            self.updated_at = timezone.now()
        super().save(*args, **kwargs)

class IdeaStar(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.idea.title