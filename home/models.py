from django.db import models
import datetime
# Django models import
# Create your models here.

# MenuCategory model banaya jo menu ki categories store karega
class MenuCategory(models.Model):
    # name field jisme category ka naam store hoga (unque hona chahiye)
    name = models.CharField(max_length=100, unque=True)

class DailySpecialManager(models.Manager):
    def upcoming(self):
        today = datetime.date.today()
        return self.filter(special_date__gte=today)

class DailySpecial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    special_date = model.DateField()
    objects = DailySpecialManager()
    
    @staticmethod
    def get_random_special():
        return DailySpecial.objects.order_by('?').first()
    
    def __str__(self):
        return self.name