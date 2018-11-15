from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns=[
url(r'^$',views.home),
url(r'^logintest/$',views.logintest),
url(r'^signup/$',views.make),
url(r'^signup/makeaccount/$',views.makeaccount),

]