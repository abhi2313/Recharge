from django.db import models

# Create your models here.


class Recharge(models.Model):
    recharge_amount = models.IntegerField()
    validity = models.IntegerField()


class SuccessfulRecharge(models.Model):
    recharge = models.ForeignKey(Recharge, on_delete=models.CASCADE)
