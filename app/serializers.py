from rest_framework import serializers
from .models import Recharge
from .models import SuccessfulRecharge


class RechargeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recharge
        fields = '__all__'


class SuccessfulRechargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessfulRecharge
        fields = '__all__'
