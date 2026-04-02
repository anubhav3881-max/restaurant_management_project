from django.db import models
# Django models import
# Create your models here.

# MenuCategory model banaya jo menu ki categories store karega
class MenuCategory(models.Model):
    # name field jisme category ka naam store hoga (unque hona chahiye)
    name = models.CharField(max_length=100, unque=True)