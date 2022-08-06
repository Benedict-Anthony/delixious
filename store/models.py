from re import M
from django.db import models
from users.models import Customer
# Create your models here.

class Category(models.Model):
    type = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.type

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to="images")
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    description = models.TextField(max_length=200, null=True, default="")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url   
    
    @property
    def discountPrice(self):
        try:
            discpr = self.discount
        except:
            discpr = ""
        return discpr
    
    def get_product(self):
        name = f"{self.name}"
        return name
    
    
    def __str__(self):
        return self.name
    
    
class OrderDetail(models.Model):
    status = [
        ("pending", "pending"),
        ("sent","sent"),
        ("deliverd", "deliverd")
    ] 
    
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=50, choices=status, default="pending")
    completed = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    transanction_id = models.SlugField(max_length=15)
    
    class Meta:
        verbose_name_plural ="Order Details"
        
    def __str__(self):
        return f"{self.customer}" 
    
    
    def __int__(self):
        return int(self.id )
   
  
    
class ShippingInfo(models.Model):
    orderDetails = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    
    def __str__(self):
        return f"{self.state} {self.city}"
   

class TransactionDetails(models.Model):
    transaction_id = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    amout = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.transaction_id
   
class OrderItems(models.Model):
    orderDetails = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True, default=0)
    total_amout = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shippingInfo = models.ForeignKey(ShippingInfo, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_id = models.ForeignKey(TransactionDetails, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        verbose_name_plural ="Ordered Items"

    
    def __str__(self):
        return self.product.name

