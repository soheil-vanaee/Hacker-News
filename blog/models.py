from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    little_slug = models.CharField(max_length=20)
    Article_External_Link = models.CharField(max_length=100 ,blank=True)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=100)
    author = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
        