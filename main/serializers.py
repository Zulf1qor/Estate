from .models import *
from rest_framework import serializers

class EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estate
        fields = "__all__"


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"


class AgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = "__all__"


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"


class History_contractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = History_contracts
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class Payment_receiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentReciept
        fields = "__all__"


class CassaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cassa
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"