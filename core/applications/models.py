from django.db import models

class ApplicationLog(models.Model):
    city = models.CharField(max_length=100)
    success = models.BooleanField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)