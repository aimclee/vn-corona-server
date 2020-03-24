from django.db import models

# Create your models here.


class Nhandan_Title(models.Model):
    news_title = models.CharField(max_length=255)
    page_link = models.URLField()
    summary = models.TextField()
    img = models.URLField()
    
    def __str__(self):
        return self.news_title
    
class VnExpress (models.Model):
    news_title = models.CharField(max_length=255)
    page_link = models.URLField()
    summary = models.TextField()
    img = models.URLField()
    def __str__(self):
        return self.news_title


class Moh_Number(models.Model):
    moh_number = models.CharField(max_length=100)
    def __str__(self):
        return self.moh_number
    

class Moh_Tracker(models.Model):
    location = models.CharField(max_length=100)
    tracker = models.TextField()
    def __str__(self):
        return self.location
    