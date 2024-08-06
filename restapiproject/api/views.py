from rest_framework import generics
from .models import PhoneNumber
from .serializers import PhoneNumberSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is a sample API by Melika:)")

class PhoneNumberListCreate(generics.ListCreateAPIView):
    queryset = PhoneNumber.objects.all()
    serializer_class = PhoneNumberSerializer


