from django.utils import timezone
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView , UpdateAPIView , DestroyAPIView
import random
from app_transaction.models import *
from app_transaction.api.serializers import *
from django.db.models import Sum
from rest_framework.generics import ListAPIView


class CreateTransaction(CreateAPIView) :

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)


class ShowTransaction(RetrieveAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class UpdateTransaction(UpdateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class DeleteTransaction(DestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def destroy(self, request, *args, **kwargs):

        transaction = self.get_object()
        transaction.delete()

        return Response(
            {'status': 'ok', 'message': 'Transaction was successfully deleted.'},
            status=status.HTTP_204_NO_CONTENT)
    

class TransactionListView(ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)


class TransactionReportView(ListAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionSerializer

    def list(self, request, *args, **kwargs):

        query_serializer = TransactionReportQuerySerializer(data=request.query_params)
        query_serializer.is_valid(raise_exception=True)
        data = query_serializer.validated_data #یک دیکشنریه که همه اطلاعات معتبر رو داخل خودش داره

        queryset = Transaction.objects.filter(
            user=request.user,
            date__range=[data['start_date_gregorian'], data['end_date_gregorian']],)

        income_total = queryset.filter(type='income').aggregate(total=Sum('amount'))['total'] or 0
        expense_total = queryset.filter(type='expense').aggregate(total=Sum('amount'))['total'] or 0

        category_totals = (
            queryset.values('category__id', 'category__title')
            .annotate(total=Sum('amount'))
            .order_by('-total'))

        serializer = self.get_serializer(queryset, many=True) #این خط صرفا تراکنش هارو میگیره از مدل سریالایزر

        return Response({
            'period': data['period'],
            'start_date': data['start_date_jalali'],
            'end_date': data['end_date_jalali'],
            'income_total': income_total,
            'expense_total': expense_total,
            'balance': income_total - expense_total,
            'category_totals': list(category_totals),
            'transactions': serializer.data,
        })