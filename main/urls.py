from django.urls import path
from .views import *

urlpatterns = [
    path('estate-filter_by_id/', estate_filter_by_id),
    path('estate-filter_by_price/', estate_filter_by_price),
    path('estate-filter_by_type/', estate_filter_by_type),
    path('estate-filter_by_rooms/', estate_filter_by_rooms),
    path('estate-filter_by_status/', estate_filter_by_status),
    path('estate-filter_by_location/', estate_filter_by_location),
    path('customer-filter_by_name/', customer_filter_by_name),
    path('customer-filter_by_password/', customers_filter_by_password),
    path('customer-filter_by_password_number/', customers_filter_by_password_number),
    path('agents-filter_by_name/', agents_filter_by_name),
    path('agents-filter_by_age/', agents_filter_by_age),
    path('agents-filter_by_salary/', agents_filter_by_salary),
    path('meeting-filter_by_date/', meeting_filter_by_date),
    path('building-filter_by_id/', building_filter_by_id),
    path('building-filter_by_location/', building_filter_by_location),
    path('building-filter_by_price/', building_filter_by_price),
    path('building-filter_by_rooms/', building_filter_by_rooms),
    path('building-filter_by_rent/', building_filter_by_rent),
    path('history-filter_by_number/', history_filter_by_number),
    path('history-filter_by_date/', history_filter_by_date),
    path('cassa-filter_by_name/', cassa_filter_by_name),
    path('payment-filter_by_payment_date/', payment_filter_by_payment_date),
    path('paymentreceipt-filter_by_payment/', paymentreceipt_filter_by_payment),
]