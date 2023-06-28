from django.db import models

#イベント情報モデル
class Event(models.Model):
    user = models.CharField(max_length=255,default='')
    data = models.JSONField()

#参加者情報モデル
class Participant(models.Model):    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    data = models.JSONField()