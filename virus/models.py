from django.db import models

# Create your models here.


class Nhandan_Title(models.Model):
    news_title = models.CharField(max_length=255)
    summary = models.TextField()
    img = models.URLField()
    def __str__(self):
        return self.news_title
    