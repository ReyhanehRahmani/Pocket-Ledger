from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    
    class Meta:
        unique_together = ['user', 'title']  # جلوگیری از تکراری بودن دسته‌بندی برای هر کاربر
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"

class Card(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=20)

    class Meta:
        unique_together = ['user', 'card_number']
    
    def __str__(self):
        return f"{self.bank_name} - {self.user.username}"

class Transaction(models.Model):

    class Type(models.TextChoices):
        INCOME = "income", "درآمد"
        EXPENSE = "expense", "هزینه"
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=10, choices=Type.choices)
    amount = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.get_type_display()}: {self.title} - {self.amount} تومان"
