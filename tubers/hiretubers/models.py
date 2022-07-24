from django.db import models
from django.utils import timezone

# Create your models here.
class Hiretubers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    message = models.TextField(blank=True)    
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=timezone.now)

    def __str__(self):
        return self.email