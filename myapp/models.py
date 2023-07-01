from django.db import models

#イベント情報モデル
class Event(models.Model):
    user = models.CharField(max_length=255, default='')
    event_name = models.CharField(max_length=255, default='Event Name') 
    timestamp = models.DateTimeField(default='2023-01-01 00:00:00')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data = models.JSONField()
