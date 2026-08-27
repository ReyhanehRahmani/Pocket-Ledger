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


class CreateTransaction(CreateAPIView) :

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)


class ShowTransaction(RetrieveAPIView):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class UpdateTransaction(UpdateAPIView):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class DeleteTransaction(DestroyAPIView):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
        
    def destroy(self, request, *args, **kwargs):

        transaction = self.get_object()
        transaction.delete()

        return Response(
            {'status': 'ok', 'message': 'Transaction was successfully deleted.'},
            status=status.HTTP_204_NO_CONTENT)