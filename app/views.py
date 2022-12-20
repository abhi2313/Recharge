from django.shortcuts import render
from .models import Recharge, SuccessfulRecharge
from .serializers import RechargeSerializer, SuccessfulRechargeSerializer
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView


class Get_All_recharges(APIView):
    def get(self, request):
        recharges = Recharge.objects.all()
        serializer = RechargeSerializer(recharges, many=True)
        return Response(serializer.data)


class Successful_recharges(APIView):
    def get(self, request):
        successful_recharges = SuccessfulRecharge.objects.all()
        serializer = SuccessfulRechargeSerializer(
            successful_recharges, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = SuccessfulRechargeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
