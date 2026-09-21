from rest_framework import serializers
from app_transaction.models import Transaction
import jdatetime
from rest_framework import serializers
from app_transaction.api import utils
from app_transaction.models import Transaction, Category, Card

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'bank_name', 'card_number']

class TransactionSerializer(serializers.ModelSerializer):

    bank_name = serializers.SerializerMethodField()
    card_number = serializers.SerializerMethodField()
    category_title = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = [
            'id',
            'title',
            'description',
            'type',
            'amount',
            'category',
            'category_title',
            'card',
            'bank_name',
            'card_number',
            'date',
        ]


    def get_bank_name(self,obj):
        if obj.card:
            return obj.card.bank_name
        return None
    
    def get_card_number(self,obj):
        if obj.card:
            return obj.card.card_number
        return None
    
    def get_category_title(self,obj):
        if obj.category:
            return obj.category.title
        return None


class TransactionReportQuerySerializer(serializers.Serializer):

    PERIOD_CHOICES = ['day', 'week', 'month', 'year', 'custom']

    period = serializers.ChoiceField(choices=PERIOD_CHOICES)

    year = serializers.IntegerField(required=False)
    month = serializers.IntegerField(required=False)
    day = serializers.IntegerField(required=False)
    week_number = serializers.IntegerField(required=False)

    start_date = serializers.CharField(required=False)
    end_date = serializers.CharField(required=False)

    def validate(self, attrs):

        period = attrs['period']

        try:
            if period == 'day':
                self._require(attrs, ['year', 'month', 'day'])
                j_start, j_end = utils.get_day_range(attrs['year'], attrs['month'], attrs['day'])

            elif period == 'month':
                self._require(attrs, ['year', 'month'])
                j_start, j_end = utils.get_month_range(attrs['year'], attrs['month'])

            elif period == 'year':
                self._require(attrs, ['year'])
                j_start, j_end = utils.get_year_range(attrs['year'])

            elif period == 'week':
                self._require(attrs, ['year', 'month', 'week_number'])
                j_start, j_end = utils.get_week_of_month_range(
                    attrs['year'], attrs['month'], attrs['week_number']
                )

            elif period == 'custom':
                self._require(attrs, ['start_date', 'end_date'])
                j_start, j_end = utils.get_custom_range(attrs['start_date'], attrs['end_date'])

        except ValueError as e:
            raise serializers.ValidationError({'detail': str(e)})

        attrs['start_date_gregorian'] = j_start.togregorian()
        attrs['end_date_gregorian'] = j_end.togregorian()
        attrs['start_date_jalali'] = j_start.strftime('%Y-%m-%d')
        attrs['end_date_jalali'] = j_end.strftime('%Y-%m-%d')

        return attrs

    def _require(self, attrs, fields):

        """این یک تابع کمکیه که چک می‌کنه آیا فیلدهای لازم برای اون بازه خاص واقعاً پر شدن یا نه"""
        
        missing = [f for f in fields if attrs.get(f) in (None, '')]
        
        if missing:
            raise serializers.ValidationError(
                {f: f'برای period={attrs["period"]} این فیلد الزامی است.' for f in missing}
            )