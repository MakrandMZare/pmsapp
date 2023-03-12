from django.contrib import admin
from . models import Customer, Product, UserRegister, Employee

# Register your admin.ModelAdmin here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category','product_image']
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','mobile','state','zipcode']
    
@admin.register(UserRegister)
class UserRegisterModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','lastname','mobile','email','password1','password2']
    
@admin.register(Employee)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','lastname','mobile','email','password1','password2']