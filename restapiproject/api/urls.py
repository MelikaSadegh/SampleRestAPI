from django.urls import path
from .views import PhoneNumberListCreate

urlpatterns = [
    path('phone-numbers/', PhoneNumberListCreate.as_view(), name='phone-number-list-create'),
]
