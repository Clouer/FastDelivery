from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Meta:
        db_table = 'users'


class MealCategory(models.Model):
    class Meta:
        db_table = 'categories'

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Meal(models.Model):
    class Meta:
        db_table = 'meals'

    title = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=400)
    picture = models.CharField(max_length=400)
    category = models.ForeignKey(MealCategory, on_delete=models.CASCADE, related_name='meals')

    def __str__(self):
        return self.title


class Order(models.Model):
    class Meta:
        db_table = 'orders'

    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('cooking', 'Готовится'),
        ('on_the_way', 'В пути'),
        ('delivered', 'Доставлен')
    )
    date = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default='new')
    email = models.EmailField(blank=True, default='')
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=400)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    meals = models.ManyToManyField(Meal, related_name='orders')

    def __str__(self):
        return f'Заказ номер {self.id}'
