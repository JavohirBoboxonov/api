from rest_framework import serializers
from product.models import *

class BookSerializer(Book):
    class Meta:
        model = 'Book',
        fields = '__all__',