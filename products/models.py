from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.DateTimeField(default=False)
    # Now run the command
    # python manage.py makemigrations
    # python manahe.py migrate

    def __str__(self):
        return str(self.item_name)

class Restaurant(models.Model):
    name = CharField(max_length= 100)
    address = models.TextField()
    has_delivery = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    # Now run the command
    # py manage.py makemigrations
    # py manage.py migrate

    