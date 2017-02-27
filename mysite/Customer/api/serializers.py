import json
from django.core import serializers
from rest_framework import serializers
from Customer.models import Order, Total_Orders
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    URLField,
    )


