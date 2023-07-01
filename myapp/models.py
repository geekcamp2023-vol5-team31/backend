from django.db import models

#イベント情報モデル
class Event(models.Model):
    user = models.CharField(max_length=255,default='')
    data = models.JSONField()
