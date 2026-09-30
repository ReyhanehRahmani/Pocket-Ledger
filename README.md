<div dir="rtl">

# دفترچه | Pocket Ledger

<p align="center">
  <strong>یک سیستم مدیریت مالی شخصی، مینیمال و مدرن برای ثبت، مدیریت و تحلیل درآمد و هزینه‌ها</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-6.0.6-0b4d3b?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/DRF-3.17.1-ae6b7a?style=for-the-badge" alt="Django REST Framework">
  <img src="https://img.shields.io/badge/JWT-Authentication-2b2f33?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT">
  <img src="https://img.shields.io/badge/RTL-Persian-8fAE87?style=for-the-badge" alt="RTL">
</p>

</div>

---

## ✦ درباره پروژه

**Pocket Ledger** یک اپلیکیشن مدیریت مالی شخصی است که با هدف ساده‌کردن ثبت و بررسی تراکنش‌های روزمره ساخته شده است.

تمرکز پروژه فقط روی CRUD ساده نیست؛ بک‌اند با **Django REST Framework** طراحی شده و احراز هویت، مدیریت حساب کاربری، تأیید ایمیل با OTP، بازیابی رمز عبور، گزارش‌های دوره‌ای بر اساس تقویم جلالی و خروجی Excel را پوشش می‌دهد.

رابط کاربری نیز به‌صورت **RTL و فارسی** طراحی شده و از یک زبان بصری مینیمال و Dark استفاده می‌کند:

- پس‌زمینه زغالی تیره
- سطوح خاکستری نزدیک به مشکی
- سبز ملایم برای درآمد
- رز/صورتی تیره برای هزینه
- رنگ استخوانی برای عناصر اصلی و CTAها
- فونت **Vazirmatn**
- طراحی خلوت و مبتنی بر خوانایی اطلاعات مالی

> هدف Pocket Ledger این است که اطلاعات مالی را بدون شلوغی و پیچیدگی اضافی، در قالب یک دفتر مالی دیجیتال در اختیار کاربر قرار دهد.

---

## ✨ قابلیت‌ها

### 🔐 حساب کاربری و امنیت

- ثبت‌نام با ایمیل
- ارسال کد تأیید ایمیل **OTP**
- محدودسازی درخواست‌های OTP برای جلوگیری از abuse
- ورود با **JWT**
- Refresh Token
- بازیابی رمز عبور با OTP
- توکن تأیید موقت با TTL پنج دقیقه
- اعتبارسنجی رمز عبور
- پروفایل کاربر
- تغییر نام کاربری
- انتخاب آواتار

### 💰 مدیریت تراکنش‌ها

هر کاربر فقط به اطلاعات مالی خودش دسترسی دارد.

امکانات:

- ثبت تراکنش جدید
- مشاهده جزئیات تراکنش
- ویرایش تراکنش
- حذف تراکنش
- مشاهده لیست تراکنش‌ها
- تفکیک درآمد و هزینه
- مبلغ و توضیحات
- اتصال تراکنش به دسته‌بندی
- اتصال تراکنش به کارت بانکی
- ثبت تاریخ تراکنش

### 🏷️ دسته‌بندی‌ها

- ساخت دسته‌بندی شخصی
- مشاهده دسته‌بندی‌ها
- ویرایش
- حذف
- جلوگیری از ایجاد دسته‌بندی تکراری برای یک کاربر

### 💳 کارت‌های بانکی

- ثبت کارت بانکی
- نگهداری نام بانک و شماره کارت
- ویرایش کارت
- حذف کارت
- جلوگیری از ثبت شماره کارت تکراری برای یک کاربر

### 📊 گزارش مالی

گزارش‌ها می‌توانند بر اساس بازه زمانی موردنظر تولید شوند و شامل موارد زیر هستند:

- مجموع درآمد
- مجموع هزینه
- موجودی/Balance
- مجموع مبالغ بر اساس دسته‌بندی
- لیست تراکنش‌های بازه
- تاریخ شروع و پایان بازه
- پشتیبانی از تاریخ جلالی

بازه‌های گزارش شامل:

- روز
- هفته
- ماه
- سال
- بازه دلخواه

### 📥 خروجی Excel

گزارش مالی قابلیت خروجی گرفتن به‌صورت فایل Excel را دارد.

فایل خروجی با ساختار گزارش مالی پروژه و استایل‌دهی اختصاصی تولید می‌شود تا برای نگهداری یا بررسی خارج از اپلیکیشن قابل استفاده باشد.

---

## 🎨 Design System

رابط کاربری Pocket Ledger بر پایه یک تم Dark مینیمال ساخته شده است.

| Token | Value | کاربرد |
|---|---|---|
| `--bg` | `#14171a` | پس‌زمینه اصلی |
| `--surface` | `#1b1f23` | کارت‌ها و سطوح اصلی |
| `--surface-2` | `#20242a` | ورودی‌ها و سطوح ثانویه |
| `--border` | `#2a2f35` | خطوط و مرزبندی |
| `--text` | `#e9e7e2` | متن اصلی |
| `--text-muted` | `#8f969d` | متن ثانویه |
| `--income` | `#8fae87` | درآمد |
| `--expense` | `#c07687` | هزینه |
| `--ring` | `#dcd8ce` | CTA و focus |

### UI Principles

- **Minimal first:** کمترین المان ممکن برای بیشترین خوانایی
- **Data first:** اطلاعات مالی در اولویت بصری قرار دارند
- **Semantic colors:** رنگ‌ها معنای مشخص دارند
- **RTL native:** رابط از ابتدا برای زبان فارسی و راست‌به‌چپ طراحی شده
- **Low-noise UI:** بدون گرادیان‌های سنگین و عناصر تزئینی غیرضروری
- **Responsive layout:** ساختار اصلی برای نمایشگرهای مختلف قابل استفاده است

---

## 🧱 معماری پروژه

ساختار اصلی پروژه به چند Django App با مسئولیت‌های مشخص تقسیم شده است:

```text
PocketLedger/
│
├── PocketLedger/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── app_account/
│   ├── api/
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   └── views.py
│   ├── models.py
│   └── admin.py
│
├── app_transaction/
│   ├── api/
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── utils.py
│   │   └── views.py
│   ├── management/
│   │   └── commands/
│   │       └── seed_data.py
│   ├── models.py
│   └── admin.py
│
├── app_email/
│   ├── templates/
│   │   └── otp.html
│   ├── utils.py
│   └── models.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── avatars/
│
├── manage.py
├── requirements.txt
└── .env.example
```

### مسئولیت Appها

| App | مسئولیت |
|---|---|
| `app_account` | احراز هویت، OTP، ثبت‌نام، بازیابی رمز و پروفایل |
| `app_transaction` | تراکنش‌ها، دسته‌بندی‌ها، کارت‌ها و گزارش مالی |
| `app_email` | ارسال ایمیل و قالب OTP |
| `PocketLedger` | تنظیمات و routing اصلی پروژه |
| `templates` | رابط کاربری اصلی |

---

## 🗃️ مدل داده

مدل مالی پروژه حول سه موجودیت اصلی ساخته شده است:

```text
User
 │
 ├── Category
 │
 ├── Card
 │
 └── Transaction
       ├── Category
       └── Card
```

### Transaction

```text
Transaction
├── user
├── title
├── description
├── type
├── amount
├── category
├── card
└── date
```

نوع تراکنش:

```text
income
expense
```

### Category

هر دسته‌بندی به یک کاربر تعلق دارد و برای همان کاربر باید یکتا باشد.

### Card

هر کارت نیز متعلق به یک کاربر است و شماره کارت برای همان کاربر تکراری نیست.

---

## 🔌 API

Base URL:

```text
/api/
```

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/account/otp/send/` | ارسال OTP |
| `POST` | `/api/account/otp/verify/` | تأیید OTP |
| `POST` | `/api/account/register/` | ثبت‌نام |
| `POST` | `/api/account/password/reset/` | بازیابی رمز |
| `GET` | `/api/account/profile/` | دریافت پروفایل |
| `PATCH` | `/api/account/profile/` | ویرایش پروفایل |
| `POST` | `/api/token/` | دریافت JWT |
| `POST` | `/api/token/refresh/` | Refresh Token |

### Transactions

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/transaction/create/` | ایجاد تراکنش |
| `GET` | `/api/transaction/show/<id>/` | مشاهده تراکنش |
| `PUT/PATCH` | `/api/transaction/update/<id>/` | ویرایش |
| `DELETE` | `/api/transaction/delete/<id>/` | حذف |
| `GET` | `/api/transaction/all-transactions/` | لیست تراکنش‌ها |
| `GET` | `/api/transaction/report/` | گزارش مالی |

### Categories & Cards

| Method | Endpoint | Description |
|---|---|---|
| `GET/POST` | `/api/transaction/categories/` | لیست / ایجاد دسته‌بندی |
| `GET/PATCH/DELETE` | `/api/transaction/categories/<id>/` | مدیریت دسته‌بندی |
| `GET/POST` | `/api/transaction/cards/` | لیست / ایجاد کارت |
| `GET/PATCH/DELETE` | `/api/transaction/cards/<id>/` | مدیریت کارت |

---

## 📚 API Documentation

برای مشاهده مستندات API در محیط توسعه:

### Swagger

```text
http://127.0.0.1:8000/swagger/
```

### ReDoc

```text
http://127.0.0.1:8000/redoc/
```

همچنین schema خام Swagger در دسترس است:

```text
http://127.0.0.1:8000/swagger.json
```

---

## 🚀 نصب و اجرا

### 1. Clone

```bash
git clone <repository-url>
cd PocketLedger
```

### 2. ساخت Virtual Environment

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. نصب Dependencies

```bash
pip install -r requirements.txt
```

### 4. تنظیم Environment Variables

فایل نمونه را کپی کنید:

```bash
cp .env.example .env
```

سپس مقادیر موردنیاز را در `.env` قرار دهید:

```env
SECRET_KEY=your-secret-key
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

> فایل `.env` را در Git commit نکنید.

### 5. اجرای Migration

```bash
python manage.py migrate
```

### 6. ساخت Superuser

```bash
python manage.py createsuperuser
```

### 7. اجرای Development Server

```bash
python manage.py runserver
```

سپس:

```text
http://127.0.0.1:8000/
```

---

## 🌱 Seed Data

برای ایجاد داده‌های آزمایشی می‌توان از management command پروژه استفاده کرد:

```bash
python manage.py seed_data
```

مقادیر پیش‌فرض:

- ۲ کاربر آزمایشی
- ۲۰ تراکنش برای هر کاربر
- دسته‌بندی‌های نمونه
- کارت‌های بانکی نمونه
- تراکنش‌های تصادفی در بازه ۶ ماه گذشته

### شخصی‌سازی Seed

تعداد کاربران:

```bash
python manage.py seed_data --users 5
```

تعداد تراکنش برای هر کاربر:

```bash
python manage.py seed_data --transactions 50
```

ترکیب هر دو:

```bash
python manage.py seed_data --users 5 --transactions 50
```

پاک‌کردن داده‌های مالی قبلی قبل از Seed:

```bash
python manage.py seed_data --delete
```

---

## 🔑 Authentication Flow

فرآیند ثبت‌نام به‌صورت مرحله‌ای انجام می‌شود:

```text
Email
  │
  ▼
Send OTP
  │
  ▼
Verify OTP
  │
  ▼
Verification Token
  │
  ▼
Register
  │
  ▼
Access + Refresh JWT
```

بازیابی رمز عبور نیز از flow مشابهی استفاده می‌کند:

```text
Email
  │
  ▼
Password Reset OTP
  │
  ▼
Verify OTP
  │
  ▼
Temporary Verification Token
  │
  ▼
Set New Password
```

برای OTP محدودیت نرخ درخواست تعریف شده است:

```text
OTP Send   → 5 requests / hour
OTP Verify → 10 requests / hour
```

---

## 📅 تاریخ جلالی

Pocket Ledger برای گزارش‌های مالی از **Jalali / Persian Calendar** پشتیبانی می‌کند.

توابع کمکی موجود در پروژه امکان ساخت بازه‌های:

```text
Day
Week
Month
Year
Custom Range
```

را فراهم می‌کنند و در کنار آن تاریخ میلادی موردنیاز برای Query دیتابیس نیز مدیریت می‌شود.

---

## 🛠️ Tech Stack

### Backend

- Python
- Django
- Django REST Framework
- Simple JWT
- PyJWT
- drf-yasg
- SQLite

### Authentication & Email

- JWT Authentication
- Email OTP
- Gmail SMTP
- Django Email Utilities

### Date & Localization

- `jdatetime`
- Jalali Calendar
- RTL Persian UI
- Vazirmatn

### Frontend

- HTML5
- CSS3
- Vanilla JavaScript
- SVG-based data visualization
- ExcelJS برای خروجی Excel

---

## 🧪 Development Notes

### API Security

Endpointهای مربوط به داده‌های مالی با:

```python
IsAuthenticated
```

محافظت می‌شوند و QuerySet تراکنش‌ها بر اساس کاربر احراز هویت‌شده محدود می‌شود.

به‌عنوان نمونه:

```python
Transaction.objects.filter(user=self.request.user)
```

این الگو باعث می‌شود کاربر فقط منابع متعلق به خودش را دریافت یا مدیریت کند.

### Admin Panel

پنل Django Admin برای مدیریت:

- Users
- Categories
- Cards
- Transactions

پیکربندی شده است و برای تراکنش‌ها امکان filtering، searching و date hierarchy نیز وجود دارد.

---

## 📁 Git Branches

در repository فعلی branchهای اصلی پروژه شامل موارد زیر هستند:

```text
master
dev
frontend
```

پیشنهاد workflow توسعه:

```text
feature/*
   ↓
dev
   ↓
master
```

---

## 🔒 نکات امنیتی مهم

قبل از Deploy پروژه:

- `DEBUG` را خاموش کنید.
- `SECRET_KEY` را در Environment Variable نگه دارید.
- App Password ایمیل را هرگز commit نکنید.
- `ALLOWED_HOSTS` را محدود کنید.
- تنظیمات CORS را برای محیط production محدود کنید.
- فایل `.env` را از repository خارج نگه دارید.
- در صورت افشای هر secret، آن را rotate کنید.

> اگر این repository قبلاً شامل secret واقعی بوده است، صرفاً حذف secret از فایل کافی نیست؛ credential افشاشده باید از سمت سرویس مربوطه نیز باطل و جایگزین شود.

---

## 🗺️ مسیر توسعه پیشنهادی

برخی قابلیت‌هایی که می‌توانند در نسخه‌های بعدی اضافه شوند:

- [ ] بودجه‌بندی ماهانه
- [ ] اهداف مالی
- [ ] recurring transactions
- [ ] فیلتر پیشرفته تراکنش‌ها
- [ ] نمودار روند درآمد و هزینه
- [ ] اعلان‌های مالی
- [ ] چند ارز
- [ ] PostgreSQL برای production
- [ ] تست‌های واحد و API گسترده‌تر
- [ ] Docker
- [ ] CI/CD
- [ ] deployment configuration

---

## 👩‍💻 هدف پروژه

Pocket Ledger به‌عنوان یک پروژه Full-Stack با تمرکز ویژه روی **Backend Development، طراحی REST API، احراز هویت، مدیریت داده‌های مالی و تجربه کاربری فارسی/RTL** توسعه داده شده است.

این پروژه علاوه بر ارائه یک ابزار کاربردی برای مدیریت مالی شخصی، نمونه‌ای از پیاده‌سازی یک معماری Django + REST API در یک پروژه واقعی‌تر از CRUDهای ساده است.

---

<p align="center">
  Built with Django · DRF · JWT · Python
</p>
