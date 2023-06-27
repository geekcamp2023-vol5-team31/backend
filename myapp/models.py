from django.db import models
from django.contrib.auth.models import User

#イベント情報モデル
class Event(models.Model):
    name = models.CharField(max_length=200) #イベント名
    date = models.DateTimeField()           #日付

#参加者情報モデル
class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)                    #参加者名
    event = models.ForeignKey(Event, on_delete=models.CASCADE)                  #イベント名
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)           #総額
    collection_amount = models.DecimalField(max_digits=8, decimal_places=2)     # 徴収額
    return_amount = models.DecimalField(max_digits=8, decimal_places=2)         # 返す金額