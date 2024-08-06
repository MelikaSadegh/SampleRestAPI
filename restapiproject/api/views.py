from rest_framework import generics
from .models import PhoneNumber
from .serializers import PhoneNumberSerializer

class PhoneNumberListCreate(generics.ListCreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer
