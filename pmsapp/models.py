from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES=(
    ('CK', 'Cakes'),
    ('BC', 'Biscuits'),
    ('BD', 'Breads'),
    ('BK', 'Books'),
    ('BU', 'Flowers Buke'),
    ('GA', 'Gift Articles'),
)

STATE_CHOICES=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam, Bihar','Assam, Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Dadra and Nagar Haveli & Daman and Diu','Dadra and Nagar Haveli & Daman and Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu and Kashmir','Jammu and Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Ladakh','Ladakh'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry (Pondicherry)','Puducherry (Pondicherry)'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
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
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name
    
    
class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=250)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=250)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    razorpay_paymeny_id = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='Pending')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.Product.discounted_price