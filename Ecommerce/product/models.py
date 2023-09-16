from django.db import models
from django.contrib.auth.models import User
# from .managers import CustomManager

class Items(models.Model):
	name=models.CharField(max_length=40)
	image=models.ImageField(upload_to="product/my products")
	selling_price=models.FloatField()
	price=models.FloatField()
	quantity=models.IntegerField()
	available=models.BooleanField(default=True)
	desc=models.TextField()
	# objects=models.Manager() # by default
	# products=CustomManager() # filter apply

class SurfItems(models.Model):
	name=models.CharField(max_length=40)
	image=models.ImageField(upload_to="product/Surf")
	selling_price=models.FloatField()
	price=models.FloatField()
	quantity=models.IntegerField()
	available=models.BooleanField(default=True)
	desc=models.TextField() 
	# objects=models.Manager() # by default
	# products=CustomManager() # filter apply


class mobile(models.Model):
	name=models.CharField(max_length=40)
	image=models.ImageField(upload_to="product/mobile")
	selling_price=models.FloatField()
	price=models.FloatField()
	quantity=models.IntegerField()
	available=models.BooleanField(default=True)
	desc=models.TextField() 

# class CartItem(models.Model):
# 	user=models.ForeignKey(User,on_delete=models.CASCADE)
# 	product=models.ForeignKey(Items,on_delete=models.CASCADE)
# 	quantity=models.PositiveIntegerField(default=1)

# 	@property
# 	def total_cost(self):
# 		return self.quantity * self.product.price



class Transaction(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	cat=models.CharField(max_length=40)
	cat_id=models.IntegerField()
	purchased_quan=models.IntegerField()
	date=models.DateTimeField(auto_now_add=True)


class ItemModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.IntegerField()
    order_id = models.CharField(max_length = 100)
    razorpay_payment_id = models.CharField(max_length = 100,blank=True)
    paid = models.BooleanField(default=False)