from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns=[
url(r'^$',views.home),
url(r'^sign_up/$',views.sign_up),
url(r'^get_details/$',views.get_details),
url(r'^add_details/$',views.add),
url(r'^add_details/address_details/$',views.address_details),
]
