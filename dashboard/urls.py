from django.urls import path
from .views import *

urlpatterns = [
    path('estate/', CreateEstate.as_view(), name='create_estate'),
    path('estate/<int:pk>/', UpdateEstate.as_view(), name='update_estate'),
    path('estate/<int:pk>/delete/', DeleteEstate.as_view(), name='delete_estate'),
    path('estate/all/', Estateall.as_view(), name='estate_all'),

    path('customers/', CreateCustomers.as_view(), name='create_customers'),
    path('customers/<int:pk>/', UpdateCustomers.as_view(), name='update_customers'),
    path('customers/<int:pk>/delete/', DeleteCustomers.as_view(), name='delete_customers'),
    path('customers/all/', Customers_all.as_view(), name='customers_all'),
]
