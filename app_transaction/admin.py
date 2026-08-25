from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Category, Card, Transaction


# ====================== تعریف Inlineها ======================

class CategoryInline(admin.TabularInline):
    """نمایش دسته‌بندی‌های کاربر در صفحه ادمین کاربر"""
    model = Category
    extra = 1
    fields = ['title']
    show_change_link = True


class CardInline(admin.TabularInline):
    """نمایش کارت‌های کاربر در صفحه ادمین کاربر"""
    model = Card
    extra = 1
    fields = ['bank_name', 'card_number']
    show_change_link = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'id']
    list_filter = ['user']
    search_fields = ['title', 'user__username']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['bank_name', 'card_number', 'user', 'id']
    list_filter = ['user']
    search_fields = ['bank_name', 'card_number', 'user__username']


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'type', 'amount', 'date', 'category', 'card']
    list_filter = ['type', 'date', 'category', 'card', 'user']
    search_fields = ['title', 'description', 'user__username']
    date_hierarchy = 'date'
    ordering = ['-date']
    list_editable = ['type', 'amount']


class CustomUserAdmin(UserAdmin):
    inlines = [CategoryInline, CardInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)