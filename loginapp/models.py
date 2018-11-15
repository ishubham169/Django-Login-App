# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class login_table(models.Model):
	user_name=models.CharField(max_length=250)
	pass_word=models.CharField(max_length=250)
	


