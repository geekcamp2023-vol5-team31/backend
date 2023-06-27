from django.db import models

#イベント情報モデル
class Event(models.Model):
    data = models.JSONField()

#参加者情報モデル
class Participant(models.Model):    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    data = models.JSONField()