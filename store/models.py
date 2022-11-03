from django.db import models

# Create your models here.

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotion = models.ManyToManyField(Promotion)

class Customer(models.Model):
    Membership_Bronze = 'B'
    Membership_Silver = 'S'
    Membership_Gold = 'G'
    
    Membership_Choices = [
        (Membership_Bronze, 'Bronze'),
        (Membership_Silver, 'Silver'),
        (Membership_Gold, 'Gold')
        
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=Membership_Choices, default=Membership_Bronze)


class Order(models.Model):
    Pending_state = 'P'
    Complete_state = 'C'
    Failed_state = 'F'

    Payment_State = [
        (Pending_state, 'Pending'),
        (Complete_state, 'Complete'),
        (Failed_state, 'Failed'),
        
    ]
    placed_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=Payment_State, default=Pending_state )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()