from rest_framework import serializers
from .models import Borrowing, Return

class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowing
        fields = ['id', 'user', 'book', 'borrow_date', 'return_date', 'is_returned']

class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Return
        fields = ['id', 'borrowing', 'return_date', 'fine']
