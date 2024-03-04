from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


''' Start Estate filter '''
@api_view(["GET"])
def estate_filter_by_id(request):
    id = request.GET.get('id')
    estate = Estate.objects.filter(id=id)
    ser = EstateSerializer(estate, many=True)
    return Response(ser.data)


@api_view(["GET"])
def estate_filter_by_price(request):
    price = request.GET.get('price')
    estate = Estate.objects.filter(price=price)
    ser = EstateSerializer(estate, many=True)
    return Response(ser.data)


@api_view(["GET"])
def estate_filter_by_type(request):
    type = request.GET.get('type')
    estate = Estate.objects.filter(type__icontains=type)
    ser = EstateSerializer(estate, many=True)
    return Response(ser.data)


@api_view(["GET"])
def estate_filter_by_rooms(request):
    rooms = request.GET.get('rooms')
    estate = Estate.objects.filter(rooms__icontains=rooms)
    ser = EstateSerializer(estate, many=True)
    return Response(ser.data)


@api_view(["GET"])
def estate_filter_by_status(request):
    status = request.GET.get('status')
    estate = Estate.objects.filter(status__icontains=status)
    ser = EstateSerializer(estate, many=True)
    return Response(ser.data)


@api_view(["GET"])
def estate_filter_by_location(request):
    location = request.GET.get('location')
    estate = Estate.objects.filter(location=location)
    ser = EstateSerializer(estate, many=True)
    return Response(ser.data)

''' End Estate filter '''

''' Start Customers filter '''
@api_view(["GET"])
def customer_filter_by_name(request):
    name = request.GET.get('name')
    customer = Customers.objects.filter(name__icontains=name)
    ser = CustomersSerializer(customer, many=True)
    return Response(ser.data)


@api_view(["GET"])
def customers_filter_by_password(request):
    password_ser = request.GET.get('password_ser')
    customer = Customers.objects.filter(password_ser__icontains=password_ser)
    ser = CustomersSerializer(customer, many=True)
    return Response(ser.data)


@api_view(["GET"])
def customers_filter_by_password_number(request):
    password_number = request.GET.get('password_number')
    customer = Customers.objects.filter(password_number__icontains=password_number)
    ser = CustomersSerializer(customer, many=True)
    return Response(ser.data)

''' End Customers filter '''


''' Start Agents filter '''
@api_view(["GET"])
def agents_filter_by_name(request):
    name = request.GET.get('name')
    agents = Agents.objects.filter(name__icontains=name)
    ser = AgentsSerializer(agents, many=True)
    return Response(ser.data)


@api_view(["GET"])
def agents_filter_by_age(request):
    age = request.GET.get('age')
    agents = Agents.objects.filter(age__icontains=age)
    ser = AgentsSerializer(agents, many=True)
    return Response(ser.data)


@api_view(["GET"])
def agents_filter_by_salary(request):
    salary = request.GET.get('salary')
    agents = Agents.objects.filter(salary__icontains=salary)
    ser = AgentsSerializer(agents, many=True)
    return Response(ser.data)

''' End Agents filter '''


@api_view(["GET"])
def meeting_filter_by_date(request):
    date = request.GET.get('date')
    meeting = Meeting.objects.filter(date__icontains=date)
    ser = MeetingSerializer(meeting, many=True)
    return Response(ser.data)


@api_view(["GET"])
def building_filter_by_id(request):
    id = request.GET.get('id')
    building = Building.objects.filter(id__icontains=id)
    ser = BuildingSerializer(building, many=True)
    return Response(ser.data)


@api_view(["GET"])
def building_filter_by_location(request):
    location = request.GET.get('location')
    building = Building.objects.filter(location__icontains=location)
    ser = BuildingSerializer(building, many=True)
    return Response(ser.data)


@api_view(["GET"])
def building_filter_by_price(request):
    price = request.GET.get('price')
    building = Building.objects.filter(price__icontains=price)
    ser = BuildingSerializer(building, many=True)
    return Response(ser.data)


@api_view(["GET"])
def building_filter_by_rooms(request):
    rooms = request.GET.get('rooms')
    building = Building.objects.filter(rooms__icontains=rooms)
    ser = BuildingSerializer(building, many=True)
    return Response(ser.data)


@api_view(["GET"])
def building_filter_by_rent(request):
    rent = request.GET.get('rent')
    building = Building.objects.filter(rent__icontains=rent)
    ser = BuildingSerializer(building, many=True)
    return Response(ser.data)


@api_view(["GET"])
def history_filter_by_number(request):
    number = request.GET.get('number')
    history = History_contracts.objects.filter(number__icontains=number)
    ser = History_contractsSerializer(history, many=True)
    return Response(ser.data)


@api_view(["GET"])
def history_filter_by_date(request):
    date = request.GET.get('date')
    history = History_contracts.objects.filter(date__icontains=date)
    ser = History_contractsSerializer(history, many=True)
    return Response(ser.data)


@api_view(["GET"])
def payment_filter_by_payment_date(request):
    payment_date = request.GET.get('payment_date')
    payment = Payment.objects.filter(payment_date__icontains=payment_date)
    ser = PaymentSerializer(payment, many=True)
    return Response(ser.data)


@api_view(["GET"])
def paymentreceipt_filter_by_payment(request):
    payment = request.GET.get('payment')
    paymentreceipt = PaymentReciept.objects.filter(payment=payment)
    ser = Payment_receiptSerializer(paymentreceipt, many=True)
    return Response(ser.data)


@api_view(["GET"])
def cassa_filter_by_name(request):
    name = request.GET.get('name')
    cassa = Cassa.objects.filter(name__icontains=name)
    ser = CassaSerializer(cassa, many=True)
    return Response(ser.data)


