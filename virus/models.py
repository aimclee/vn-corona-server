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


class WorldMeter (models.Model):
    total_infected = models.CharField(max_length=50)
    total_death = models.CharField(max_length=50)
    total_recovery = models.CharField(max_length=50)
    new_infected = models.CharField(max_length=50)
    

class Moh_Tracker(models.Model):
    location = models.CharField(max_length=100)
    tracker = models.TextField()
    def __str__(self):
        return self.location
    