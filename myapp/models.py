from django.db import models
from django.contrib.auth.models import User

#誰がどれだけ支払ったか
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

#誰から誰へいくら移動するべきか
class Transfer(models.Model):
    pass