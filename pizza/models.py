from secrets import choice
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Order(models.Model):

    SIZES = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA_LARGE', 'extra_large'),
    )

    ORDER_STATUS = (
        ('PENDING', 'pending'),
        ('IN_PROGRESS', 'in_progress'),
        ('DELIVERED', 'delivered'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=20, choices=SIZES, default='MEDIUM',)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS, default='IN_PROGRESS')
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.__str__() + ' - ' + self.size + ' - ' + self.order_status