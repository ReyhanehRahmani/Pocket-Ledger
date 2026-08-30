from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from app_transaction.models import Category, Card, Transaction
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'پر کردن دیتابیس با داده‌های آزمایشی (Seed Data)'

    def add_arguments(self, parser):
        """اضافه کردن آرگومان‌های اختیاری"""
        parser.add_argument(
            '--users',
            type=int,
            default=2,
            help='تعداد کاربرانی که ساخته میشن (پیش‌فرض: 2)'
        )
        parser.add_argument(
            '--transactions',
            type=int,
            default=20,
            help='تعداد تراکنش برای هر کاربر (پیش‌فرض: 20)'
        )
        parser.add_argument(
            '--delete',
            action='store_true',
            help='حذف داده‌های قبلی قبل از seeding'
        )

    def handle(self, *args, **options):
        """اجرای اصلی کامند"""
        num_users = options['users']
        num_transactions = options['transactions']
        delete_existing = options['delete']

        self.stdout.write(self.style.SUCCESS('🚀 شروع فرآیند Seed Data...'))

        # حذف داده‌های قبلی اگه کاربر خواسته
        if delete_existing:
            self.delete_existing_data()

        # ایجاد داده‌ها
        users = self.create_users(num_users)
        
        for user in users:
            self.create_categories(user)
            self.create_cards(user)
            self.create_transactions(user, num_transactions)

        self.stdout.write(self.style.SUCCESS('✅ Seed Data با موفقیت انجام شد!'))

    def delete_existing_data(self):
        """حذف تمام داده‌های قبلی"""
        self.stdout.write(self.style.WARNING('🗑️ حذف داده‌های قبلی...'))
        
        Transaction.objects.all().delete()
        Category.objects.all().delete()
        Card.objects.all().delete()
        # کاربران رو حذف نمیکنیم (چون ممکنه مهم باشن)
        # ولی اگه خواستی، این خط رو فعال کن:
        # User.objects.filter(is_superuser=False).delete()
        
        self.stdout.write(self.style.SUCCESS('✅ داده‌های قبلی حذف شدند.'))

    def create_users(self, num_users):
        """ایجاد کاربران آزمایشی"""
        self.stdout.write(f'👤 ایجاد {num_users} کاربر...')
        
        users = []
        
        for i in range(1, num_users + 1):
            username = f'test_user_{i}'
            email = f'test{i}@example.com'
            
            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    'email': email,
                    'first_name': f'کاربر',
                    'last_name': f'{i}',
                }
            )
            
            if created:
                user.set_password('123456')
                user.save()
                self.stdout.write(f'   ✅ کاربر {username} ساخته شد')
            else:
                self.stdout.write(f'   ℹ️ کاربر {username} از قبل وجود داشت')
            
            users.append(user)
        
        return users

    def create_categories(self, user):
        """ایجاد دسته‌بندی‌های آزمایشی"""
        self.stdout.write(f'   📂 ایجاد دسته‌بندی‌ها برای {user.username}...')
        
        categories = [
            'خوراک', 'حمل و نقل', 'قبوض', 'تفریح', 'خرید',
            'سلامت', 'آموزش', 'پوشاک', 'مسافرت', 'سرمایه‌گذاری',
            'حقوق', 'پاداش', 'فریلنس', 'اجاره', 'سود بانکی'
        ]
        
        for category_title in categories:
            Category.objects.get_or_create(
                user=user,
                title=category_title
            )
        
        self.stdout.write(f'      ✅ {len(categories)} دسته‌بندی ساخته شد')

    def create_cards(self, user):
        """ایجاد کارت‌های بانکی آزمایشی"""
        self.stdout.write(f'   💳 ایجاد کارت‌های بانکی برای {user.username}...')
        
        banks = [
            ('ملی', '6037'),
            ('صادرات', '6219'),
            ('ملت', '6104'),
            ('تجارت', '5859'),
            ('اقتصاد نوین', '6274'),
        ]
        
        for i, (bank_name, prefix) in enumerate(banks, 1):
            # ساخت شماره کارت ۱۶ رقمی
            card_number = prefix + ''.join(str(random.randint(0, 9)) for _ in range(12))
            
            Card.objects.get_or_create(
                user=user,
                bank_name=bank_name,
                defaults={'card_number': card_number}
            )
        
        self.stdout.write(f'      ✅ {len(banks)} کارت ساخته شد')

    def create_transactions(self, user, num_transactions):
        """ایجاد تراکنش‌های آزمایشی"""
        self.stdout.write(f'   💰 ایجاد {num_transactions} تراکنش برای {user.username}...')
        
        categories = Category.objects.filter(user=user)
        cards = Card.objects.filter(user=user)
        
        if not categories or not cards:
            self.stdout.write(self.style.WARNING('      ⚠️ دسته‌بندی یا کارت کافی نیست!'))
            return

        # تاریخ شروع: ۶ ماه پیش تا امروز
        start_date = date.today() - timedelta(days=180)
        end_date = date.today()
        
        # لیست عناوین و توضیحات
        income_titles = ['حقوق', 'پاداش', 'فریلنس', 'سود سرمایه‌گذاری', 'هدیه', 'پروژه جدید']
        expense_titles = ['خرید غذا', 'بنزین', 'قبض برق', 'سینما', 'خرید لباس', 
                         'پزشکی', 'دوره آموزشی', 'اجاره', 'اینترنت', 'خرید کتاب']
        
        income_desc = ['دریافتی ماهانه', 'پاداش عالی', 'پروژه تکمیل شد', 'سود سه‌ماهه', 'تولد']
        expense_desc = ['ناهار', 'پمپ بنزین', 'پرداخت قبوض', 'تفریح', 'خرید جدید', 
                       'ویزیت پزشک', 'شهریه', 'پرداخت اجاره', 'اشتراک', 'خرید کتاب']

        for i in range(num_transactions):
            # انتخاب تصادفی نوع تراکنش (۶۰٪ هزینه، ۴۰٪ درآمد)
            is_income = random.random() < 0.4
            
            if is_income:
                type_choice = 'income'
                title = random.choice(income_titles)
                desc = random.choice(income_desc)
                amount = random.randint(100000, 5000000)  # ۱۰۰ هزار تا ۵ میلیون
            else:
                type_choice = 'expense'
                title = random.choice(expense_titles)
                desc = random.choice(expense_desc)
                amount = random.randint(10000, 2000000)  # ۱۰ هزار تا ۲ میلیون
            
            # انتخاب تصادفی تاریخ (در بازه ۶ ماه گذشته)
            days_ago = random.randint(0, 180)
            transaction_date = end_date - timedelta(days=days_ago)
            
            # انتخاب تصادفی دسته‌بندی و کارت
            category = random.choice(categories)
            card = random.choice(cards)
            
            Transaction.objects.create(
                user=user,
                title=title,
                description=desc,
                type=type_choice,
                amount=amount,
                category=category,
                card=card,
                date=transaction_date
            )
        
        self.stdout.write(f'      ✅ {num_transactions} تراکنش ساخته شد')