from django.db import models

# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    button_text = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='media/slider/%Y/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline

class Team(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    fb_link = models.CharField(max_length=250)
    insta_link = models.CharField(max_length=250)
    youtube_link = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name