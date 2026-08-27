from rest_framework import serializers
from app_transaction.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            'title',
            'description',
            'type',
            'amount',
            'category',
            'card',
            'date',
        ]