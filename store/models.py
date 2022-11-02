from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

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