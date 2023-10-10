from django.db import models
from django.contrib.auth.models import User
from pytube import extract
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vicat')
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=400)
    thumbnails = models.ImageField(upload_to='thumbnails/')
    def get_id(self):
        return extract.video_id(self.link)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='videocomment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercomment')
    comment = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} commented on {self.video}"