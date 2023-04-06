from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    usrname = models.EmailField()
    pwd = models.CharField(max_length=8)
    #off = models.ManyToOneField(Offers)
    def __str__(self):
        return self.name

class Staff(models.Model):
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=30)
    gender = models.CharField(max_length=40)
    jobrole = models.CharField(max_length=40)
    cusst = models.ManyToManyField(Customer)
    email = models.EmailField()
    def __str__(self):
        return self.name
    
class Menu(models.Model):
    food_name = models.CharField(max_length=100)
    #food_id = models.CharField(max_length=100, default="")
    food_type = models.CharField(max_length=50)
    customer = models.ManyToManyField(Customer)
    price = models.CharField(max_length=40)
    #off = models.ManyToOneField(Offers)
    #headshot = models.ImageField(upload_to='hello/media')
    def __str__(self):
        return self.food_name
    
class Payment(models.Model):
    food_name = models.CharField(max_length=100, default="")
    transactiontype = models.CharField(max_length=30)
    date = models.DateField()
    cuid = models.CharField(max_length=500, default="")
    #order=models.ManyToManyField(Customer)
    #orders = models.ManyToManyField(Orders)
    #customer_bill = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #headshot = models.ImageField(upload_to='hello/media')
    def __str__(self):
        return self.food_name
    
class Offers(models.Model):
    discount = models.CharField(max_length=100)
    discounton = models.CharField(max_length=500)
    date = models.DateField()
    order=models.ManyToManyField(Customer)
    #headshot = models.ImageField(upload_to='hello/media')
    def __str__(self):
        return self.discounton
    
class Orders(models.Model):
    #ordered_by = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #food = models.ForeignKey(Menu, on_delete=models.CASCADE)
    #foodid = models.CharField(max_length=500, default="")
    foodname = models.CharField(max_length=500, default="")
    cuid = models.CharField(max_length=500, default="")
    #def __str__(self):
     #  return self.ordered_by
    
    
class Serves(models.Model):
    served_to = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staffs = models.ForeignKey(Staff, on_delete=models.CASCADE)
    #def __str__(self):
      #  return self.served_to
 
"""   
class Foodoffer(models.Model):
    food_name=models.CharField(max_length=100)
    foodtype=models.CharField(max_length=100)
    discount=models.CharField(max_length=100)
    def __str__(self):
        return self.food_name
        
"""
    


