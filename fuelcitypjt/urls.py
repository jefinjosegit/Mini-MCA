"""fuelcitypjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from fuelcityapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('header', views.header, name='header'),

    path('pump', views.pump, name='pump'),
    path('customer', views.customer, name='customer'),
    path('dboyreg', views.dboyreg, name='dboyreg'),
    path('login/', views.login, name='login'),



    path('dboyhome', views.dboyhome, name='dboyhome'),

    path('adminhome', views.adminhome, name='adminhome'),
    path('adminpump', views.adminpump, name='adminpump'),
    path('adminupdateuser', views.adminupdateuser, name='adminupdateuser'),
    path('admincustomer', views.admincustomer, name='admincustomer'),
    path('adminfuel', views.adminfuel, name='adminfuel'),
    path('admineditfuel', views.admineditfuel, name='admineditfuel'),

    path('customerhome', views.customerhome, name='customerhome'),
    path('customersearch', views.customersearch, name='customersearch'),
    path('customerrequest', views.customerrequest, name='customerrequest'),
    path('customerrequeststatus', views.customerrequeststatus,
         name='customerrequeststatus'),
    path('payment', views.payment, name='payment'),


    path('pumphome', views.pumphome, name='pumphome'),
    path('pumpstock', views.pumpstock, name='pumpstock'),
    path('pumprequest', views.pumprequest, name='pumprequest'),
    path('pumpallocate', views.pumpallocate, name='pumpallocate'),
    path('allocate', views.allocate, name='allocate'),

    path('dboyallocation', views.dboyallocation, name='dboyallocation'),
    path('delivered', views.delivered, name='delivered'),
    path('dballotments', views.dballotments, name='dballotments'),
]
