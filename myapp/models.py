from django.db import models
from jsonfield import JSONField

#イベント情報モデル
class Event(models.Model):
    data = JSONField()

#参加者情報モデル
class Participant(models.Model):    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    data = JSONField()