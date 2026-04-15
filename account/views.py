from django.shortcuts import render
from .utils import validate_phone_number
# Create your views here.

phone = request.POST.get('phone')

if not validate_phone_number(phone):
    return HttpResponse("Invalid phone number")