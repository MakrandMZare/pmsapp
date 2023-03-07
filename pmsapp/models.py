from django.db import models

# Create your models here.
CATEGORY_CHOICES=(
    ('CK', 'Cakes'),
    ('BC', 'Biscuits'),
    ('BD', 'Breads'),
    ('BK', 'Books'),
    ('BU', 'Flowers Buke'),
    ('GA', 'Gift Articles'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField(2)
    discounted_price = models.FloatField(2)
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title