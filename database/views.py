# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render,HttpResponse
from .models import customer_info,address_info,extra_info
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
	return render(request,'home.html')
def sign_up(request):
	return render(request,'database/customer_login.html')

def get_cust_id(request):
	return render(request,'database/get_details.html')
def get_details(request):
	my_id=request.GET['CUST_ID']
	a=address_info.objects.filter(cust_id=my_id)
	d=[]
	for i in a:
		d1=dict()
		d1['postcode']=i.post_code
		d1['state']=i.state
		d1['city']=i.city
		d1['cust_id']=i.cust_id.customer_id
		d1['address_id']=i.address_id
		d.append(d1)
		print(d)
	return HttpResponse(json.dumps(d), content_type="application/json")

def add_details(request):
	cust_name=request.POST['name']
	cust_email=request.POST['email']
	cust_mobile=request.POST['mobile']
	
	cust_post=request.POST['post_code']
	cust_state=request.POST['state']
	cust_city=request.POST['city']

	a=customer_info(name=cust_name,mobile=cust_mobile,email=cust_email)
	a.save()
def add(request):
	return render(request,'add_address.html')

def address_details(request):
	custom_post=request.POST['my_pin']
	custom_state=request.POST['my_state']
	custom_city=request.POST['my_city']
	custom_id=request.POST['my_id']
	a=address_info(cust_id=customer_info.objects.get(customer_id=custom_id),post_code=custom_post,state=custom_state,city=custom_city)
	a.save()
	print("shubham")
	#for i in a:
	#	print(i.cust_id.customer_id,"  ",i.post_code)
	response = HttpResponse("", status=302)
	response['Location'] = "http://127.0.0.1:8000/database/add_details/"
	return response



