# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from .models import login_table
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
	return render(request,'loginapp/abcd.html')
def make(request):
	return render(request,'loginapp/details.html')

def logintest(request):
	user = request.POST['username']
	password = request.POST['pass']
	p=login_table.objects.all()
	if( login_table.objects.filter(user_name=user, pass_word=password)):
		return render(request,'loginapp/succes.html')
	else:
		return render(request,'loginapp/login_fail.html')
def makeaccount(request):
	user=request.POST['usr']
	pd=request.POST['psw']
	us=login_table(user_name=user,pass_word=pd)
	us.save()
	response = HttpResponse("", status=302)
	response['Location'] = "http://127.0.0.1:8000/loginapp/"
	return response
	#return  HttpResponseRedirect('')
	

