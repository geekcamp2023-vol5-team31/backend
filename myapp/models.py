from django.db import models

#イベント情報モデル
class Event(models.Model):
    user = models.CharField(max_length=255, default='')
    event_name = models.CharField(max_length=255, default='Event Name')  # Default value for event_name
    timestamp = models.DateTimeField(default='2023-01-01 00:00:00')  # Default value for timestamp
    data = models.JSONField()
