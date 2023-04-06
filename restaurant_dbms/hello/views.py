from django.shortcuts import render
from django.shortcuts import HttpResponse
import os
from django.db.models.query_utils import Q
import datetime
from django.core.mail import send_mail
from hello.models import Customer,Orders,Offers,Payment,Menu

# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def menu(request):
    return render(request,"menu.html")


def msearch(request):
    discounton=request.GET.get('discounton')
    print(discounton)
    offer_list=Offers.objects.filter(discounton__icontains=discounton)
    istr='''
    <h2>Matched offers</h2>
    <table class="w3-table-all" style="width: 60%;color:black;">
      <thead>
        <tr class="w3-red">
          <th>Discount</th>
          <th>Discounton</th>
          <th>Date</th>
        </tr>
      </thead>
      
    '''
    for offer in offer_list:
        istr+="<tr><td>"+offer.discount+"</td><td>"+offer.discounton+"</td><td>"+str(offer.date)+"</td></tr>";
        
    
    return HttpResponse(istr)



def search(request):
    return render(request,"search.html")


def timing(request):
    return render(request,"timing.html")

import hashlib
def ulogin(request):
     uname=request.GET.get('usrname')
     pwd=request.GET.get('psw')
     pwd=hashlib.md5(pwd.encode('utf-8')).hexdigest()
     print(uname,pwd)
     u=Customer.objects.filter(usrname=uname,pwd=pwd)
     if(u):
        response= render(request,'home.html')
        response.set_cookie('usrname',uname)
        return response
     else:
        return render(request,'login.html')


import hashlib
def ureg(request):
    uname=request.GET.get('usrname')
    pwd=request.GET.get('psw')
    pwd=hashlib.md5(pwd.encode('utf-8')).hexdigest()
   
    email=request.GET.get('email')
    phone=request.GET.get('phone')
    city=request.GET.get('city')
    print(uname,phone,city,email,pwd)
    u=Customer(name=uname,contact=phone,city=city,usrname=email,pwd=pwd)
    u.save()
    res = send_mail("Registration", "Congratulations!. Your registration is successfull and your customer id is "+str(u.id), "brunchjnnce1485@gmail.com", [email])

    return render(request,'login.html')


import hashlib
def uorder(request):
    uname=request.COOKIES.get('usrname')
    #foodid=request.GET.get('foodid')
    foodname=request.GET.get('foodname')
    print(foodname)
    c=Customer.objects.get(usrname=uname)
    u=Orders(foodname=foodname,cuid=c.id)
    u.save()
    response = render(request,'payment.html')
    response.set_cookie('foodname',foodname)
    return response
        


import hashlib
def payorder(request):
    uname=request.COOKIES.get('usrname')
    foodname=request.COOKIES.get('foodname')
    date=request.GET.get('date')
    transactiontype=request.GET.get('transactiontype')
    print(date,transactiontype)
    c=Customer.objects.get(usrname=uname)
    email=c.usrname
    f=Orders.objects.filter(foodname=foodname)
    u=Payment(food_name=foodname,date=date,transactiontype=transactiontype,cuid=c.id)
    u.save()
    u=Customer.objects.get(usrname=email)
    res = send_mail("Food Ordering", "Your order will be ready in 30 mins your order is "+foodname+" and your customer id is "+str(c.id)+ " ordered on "+ date, "brunchjnnce1485@gmail.com", [email])

    return render(request,'payment.html')
    

def paytable(request):
    uname=request.COOKIES.get('usrname')
    #fname=request.COOKIES.get('foodname')
    c=Customer.objects.get(usrname=uname)   
    #m=Menu.objects.get(food_name=fname)
    
    istr='''
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <h2 style="text-align: center;font-weight: bolder;">Your Orders</h2>
    <table class="w3-table">
    <thead>
      <tr>
        <th>Food Name</th>
      </tr>
      </thead>
      
    '''
    food_list=Orders.objects.filter(cuid=c.id)
    #price_list=Menu.objects.filter(foodname=m.food_name)
    for food in food_list:
        istr+="<tr><td>"+str(food.foodname)+"</td></tr>";
    """for food in price_list:
        istr+="<tr><td>"+str(food.price)+"</td></tr>";"""
    return HttpResponse(istr)



def payment(request):
    return render(request,"payment.html")

def sendSimpleEmail(request):
   res = send_mail("hi", "Hope you are doing fine", "brunchjnnce1485@gmail.com", ["diyaah1102@gmail.com"])
   return HttpResponse('%s'%res)
