from django.db import models

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True) # coupon code
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2) # discount
    is_active = models.BooleanField(default=True) # active ya inactive
    valid_from = models.DateField() #start date
    valid_until = models.DateField() #end date
    def __str__(self):
        return self.code


class OrderStatus(models.Model):
    # Status name (unique hona chahiye)
    name = models.CharField(max_length=50, unique=True)
    #Example statuses
    PENDING = "Pending"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    def __str__(self):
        return self.name