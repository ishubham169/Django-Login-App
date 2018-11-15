# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class customer_info(models.Model):
	customer_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=20)
	mobile=models.CharField(max_length=10)
	email=models.CharField(max_length=30)
	def get_cust_id(self):
		return self.customer_id
	#def __str__(self):
	#	l={customer_id:self.customer_id,name:self.name,mobile:self.mobile,email:self.email}
	#	return l
class address_info(models.Model):
	address_id=models.AutoField(primary_key=True)
	cust_id=models.ForeignKey(customer_info)
	post_code=models.IntegerField()
	state=models.CharField(max_length=10)
	city=models.CharField(max_length=10)
	#def __str__(self):
	#	return str(self.address_id)+"  "+str(self.cust_id)+"  "+str(self.post_code)+"  "+str(self.state)+"  "+str(self.city)
class extra_info(models.Model):
	ex_id=models.AutoField(primary_key=True)
	cust_id=models.ForeignKey(customer_info)
	add_type=models.CharField(max_length=10)
	value=models.CharField(max_length=30)

