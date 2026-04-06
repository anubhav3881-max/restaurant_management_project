from datetime import datetime
from .models import DailyOperatingHours, Order
from django.db.models import Sum
import random
import string

def get_today_operating_hours():
    today = datetime.today().strftime('%A')

    try:
        hours = DailyOperatingHours.objects.get(day=today)
        return (hours.open_time, hours.close_time)
        except DailyOperatingHours.DoesNoteExist:
            return (None, None)

def generate_coupon_code(length=10):
    characters = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(random.choice(characters) for _ in range(length))
        # Yaha check karna hai ki code unique hai ya nahi
        # Example (agar Coupon model hai):
        # if not Coupon.objects.filter(code=code).exists():
        # return code
        return code # (agar abhi DB check nahi hai to simple return kar do)

def get_daily_sales_total(date):
    orders = Order.objects.filter(created_at__date=date)
    total = orders.aggregate(total_sum=Sum('total_price'))['total_sum']
    return total if total else 0