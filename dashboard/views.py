from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView
from main import models
from main import serializers

class CreateEstate(ListCreateAPIView):
    queryset = models.Estate.objects.all()
    ser = serializers.EstateSerializer

class UpdateEstate(UpdateAPIView):
    queryset = models.Estate.objects.all()
    ser = serializers.EstateSerializer


class DeleteEstate(DestroyAPIView):
    queryset = models.Estate.objects.all()
    ser = serializers.EstateSerializer


class Estateall(ListAPIView):
    queryset = models.Estate.objects.all()
    ser = serializers.EstateSerializer


class CreateCustomers(ListCreateAPIView):
    queryset = models.Customers.objects.all()
    ser = serializers.CustomersSerializer


class UpdateCustomers(UpdateAPIView):
    queryset = models.Customers.objects.all()
    ser = serializers.CustomersSerializer


class DeleteCustomers(DestroyAPIView):
    queryset = models.Customers.objects.all()
    ser = serializers.CustomersSerializer


class Customers_all(ListAPIView):
    queryset = models.Customers.objects.all()
    ser = serializers.CustomersSerializer


class CreateAgents(ListCreateAPIView):
    queryset = models.Agents.objects.all()
    ser = serializers.AgentsSerializer


class UpdateAgents(UpdateAPIView):
    queryset = models.Agents.objects.all()
    ser = serializers.AgentsSerializer


class DeleteCustomers(DestroyAPIView):
    queryset = models.Agents.objects.all()
    ser = serializers.AgentsSerializer


class Agents_all(ListAPIView):
    queryset = models.Agents.objects.all()
    ser = serializers.AgentsSerializer


class CretaeMeeting(ListCreateAPIView):
    queryset = models.Meeting.objects.all()
    ser = serializers.MeetingSerializer


class UpdateMeeting(UpdateAPIView):
    queryset = models.Meeting.objects.all()
    ser = serializers.MeetingSerializer


class DeleteMeeting(DestroyAPIView):
    queryset = models.Meeting.objects.all()
    ser = serializers.MeetingSerializer


class Meeting_all(ListAPIView):
    queryset = models.Meeting.objects.all()
    ser = serializers.MeetingSerializer


class CreateBuilding(ListCreateAPIView):
    queryset = models.Building.objects.all()
    ser = serializers.BuildingSerializer


class UpdateBuilding(UpdateAPIView):
    queryset = models.Building.objects.all()
    ser = serializers.BuildingSerializer


class DeleteBuilding(DestroyAPIView):
    queryset = models.Building.objects.all()
    ser = serializers.BuildingSerializer


class Building_all(ListAPIView):
    queryset = models.Building.objects.all()
    ser = serializers.BuildingSerializer


class CreateHistory_contracts(ListCreateAPIView):
    queryset = models.History_contracts.objects.all()
    ser = serializers.History_contractsSerializer


class UpdateHistory_contracts(UpdateAPIView):
    queryset = models.History_contracts.objects.all()
    ser = serializers.History_contractsSerializer


class DeleteHistory_contracts(DestroyAPIView):
    queryset = models.History_contracts.objects.all()
    ser = serializers.History_contractsSerializer


class History_contracts_all(ListAPIView):
    queryset = models.History_contracts.objects.all()
    ser = serializers.History_contractsSerializer


class CreatePayment(ListCreateAPIView):
    queryset = models.Payment.objects.all()
    ser = serializers.PaymentSerializer


class UpdatePayment(UpdateAPIView):
    queryset = models.Payment.objects.all()
    ser = serializers.PaymentSerializer


class DeletePayment(DestroyAPIView):
    queryset = models.Payment.objects.all()
    ser = serializers.PaymentSerializer


class Payment_all(ListAPIView):
    queryset = models.Payment.objects.all()
    ser = serializers.PaymentSerializer


class CreatePaymentReciept(ListCreateAPIView):
    queryset = models.PaymentReciept.objects.all()
    ser = serializers.Payment_receiptSerializer


class UpdatePaymentReciept(UpdateAPIView):
    queryset = models.PaymentReciept.objects.all()
    ser = serializers.Payment_receiptSerializer


class DeletePaymentReciept(DestroyAPIView):
    queryset = models.PaymentReciept.objects.all()
    ser = serializers.Payment_receiptSerializer


class PaymentReciept_all(ListAPIView):
    queryset = models.PaymentReciept.objects.all()
    ser = serializers.Payment_receiptSerializer


class CreateCassa(ListCreateAPIView):
    queryset = models.Cassa.objects.all()
    ser = serializers.CassaSerializer


class UpdateCassa(UpdateAPIView):
    queryset = models.Cassa.objects.all()
    ser = serializers.CassaSerializer


class DeleteCassa(DestroyAPIView):
    queryset = models.Cassa.objects.all()
    ser = serializers.CassaSerializer


class Cassa_all(ListAPIView):
    queryset = models.Cassa.objects.all()
    ser = serializers.CassaSerializer


class CreateLocation(ListCreateAPIView):
    queryset = models.Location.objects.all()
    ser = serializers.LocationSerializer


class UpdateLocation(UpdateAPIView):
    queryset = models.Location.objects.all()
    ser = serializers.LocationSerializer


class DeleteLocation(DestroyAPIView):
    queryset = models.Location.objects.all()
    ser = serializers.LocationSerializer


class Location_all(ListAPIView):
    queryset = models.Location.objects.all()
    ser = serializers.LocationSerializer
