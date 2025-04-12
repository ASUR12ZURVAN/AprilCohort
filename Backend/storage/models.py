from django.db import models

# Create your models here.
class user(models.Model):
    user_name = models.CharField(max_length = 100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=40)
    def __str__(self):
        return self.user_name
    
class call(models.Model):
    caller_number = models.CharField(max_length=40)
    call_duration = models.TimeField()
    call_instance = models.DateTimeField()  #iska matlab hai ki call kab hua tha
    avg_sentiment = models.CharField(max_length=400)

    def __str__(self):
        return self.caller_number