import jdatetime


def get_day_range(year, month, day):

    """این متد میاد یک شی تاریخ جلالی برامون میسازه"""

    j_date = jdatetime.date(year, month, day)
    return j_date, j_date


def get_month_range(year, month):

    """تاریخ دقیق شروع و پایان ماه رو تعیین میکنه"""

    start = jdatetime.date(year, month, 1)
    last_day = jdatetime.j_days_in_month[month - 1] 

    if month == 12 and jdatetime.date(year, 1, 1).isleap():
        last_day = 30

    end = jdatetime.date(year, month, last_day)

    return start, end


def get_year_range(year):

    start = jdatetime.date(year, 1, 1)
    is_leap = jdatetime.date(year, 1, 1).isleap()
    end = jdatetime.date(year, 12, 30 if is_leap else 29)
    return start, end


def get_week_of_month_range(year, month, week_number):
    """
    هفته‌ی Nام یک ماه شمسی رو برمی‌گردونه.
    هفته‌ی اول = روزهای ۱ تا ۷ ماه
    هفته‌ی دوم = روزهای ۸ تا ۱۴
    و به همین ترتیب... هفته‌ی آخر ممکنه کمتر از ۷ روز باشه.
    """
    _, month_end = get_month_range(year, month)
    last_day_of_month = month_end.day

    start_day = (week_number - 1) * 7 + 1
    end_day = min(start_day + 6, last_day_of_month)

    if start_day > last_day_of_month:
        raise ValueError(f'ماه {month} فقط تا هفته‌ی {(last_day_of_month - 1) // 7 + 1} داره.')

    start = jdatetime.date(year, month, start_day)
    end = jdatetime.date(year, month, end_day)

    return start, end


def get_custom_range(start_str, end_str):

    def parse(date_str):
        y, m, d = map(int, date_str.split('-'))
        
        return jdatetime.date(y, m, d)

    start = parse(start_str)
    end = parse(end_str)

    if start > end:
        raise ValueError('تاریخ شروع نمی‌تواند بعد از تاریخ پایان باشد.')

    return start, end