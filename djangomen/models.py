from django.db import models

# Create your models here.
from django.contrib.postgres.fields import ArrayField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class Board(models.Model):

    gasmodels_size   = ArrayField(models.CharField(max_length=200))
    name             = models.CharField(max_length=200)
    phone_number     = PhoneNumberField()
    alternate_number = PhoneNumberField(blank=True) 
    location         =ArrayField(models.FloatField(null=True,default=None), blank=True)
   
    def __str__(self):
        return self.name


class Gas(models.Model):
	brand_name = models.CharField(max_length=20)
	mass       = models.CharField(max_length=20)

	def __str__(self):
		return self.brand_name+"-"+self.mass

class Order_State(models.Model):
	order_situation	 = models.CharField(max_length=20)

	def __str__(self):
		return self.order_situation


class Order(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	order_by   = models.ForeignKey(User, null=True ,on_delete=models.SET_NULL , related_name='order_by')
	order_item = models.ForeignKey(Gas,null=True , on_delete=models.SET_NULL , related_name='order_item')
	state      =models.ForeignKey(Order_State, null=True , on_delete=models.SET_NULL , related_name='state',default=1)

	def __str__(self):
		return self.order_item.brand_name+self.order_item.mass

     