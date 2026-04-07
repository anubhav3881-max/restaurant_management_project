from django.db import models
# Django models import
# Create your models here.

# MenuCategory model banaya jo menu ki categories store karega
class MenuCategory(models.Model):
    # name field jisme category ka naam store hoga (unque hona chahiye)
    name = models.CharField(max_length=100, unque=True)

class DailySpecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    @staticmethod
    def get_random_special():
        return DailySpecial.objects.order_by('?').first()
    
    def __str__(self):
        return self.name