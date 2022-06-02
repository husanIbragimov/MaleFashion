from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from djrichtextfield.models import RichTextField
from ..blog.models import Timestamp
from colorfield.fields import ColorField


class ColorCategory(Timestamp):
    color_name = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=7, default='#FFFFFF')

    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{}</span>',
            self.color,
        )


class SizeCategory(Timestamp):
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.size


class Category(Timestamp):
    image = models.ImageField(upload_to='categories/', null=True)
    title = models.CharField(max_length=100)

    @property
    def normalize_title(self):
        return self.title.replace(' ', '').lower()

    def __str__(self):
        return self.title


class BandingCategory(Timestamp):
    image = models.ImageField(upload_to='Branding/', null=True)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.brand


class Product(Timestamp):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand_name = models.ForeignKey(BandingCategory, on_delete=models.SET_NULL, null=True)
    size = models.ManyToManyField(SizeCategory)
    name = models.CharField(max_length=250)
    price = models.FloatField()
    color = models.ManyToManyField(ColorCategory)
    mid_rate = models.FloatField(default=0)
    description = models.TextField()

    def __str__(self):
        return f'{self.id}. {self.name}'

    @property
    def get_mid_rate(self):
        rates = self.rate_set.all()
        mid = 0
        try:
            mid = sum([i.rate for i in rates]) / rates.count()
        except ZeroDivisionError:
            pass
        self.mid_rate = mid
        self.save()
        return mid


class ProductImage(Timestamp):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f'Image of {self.product}'


class Rate(Timestamp):
    RATE = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=RATE, default=0)

    def __str__(self):
        return f'Rate of {self.user.username}'





