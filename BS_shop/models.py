from django.db import models
import datetime  #here we using pics for multi tyme maybe it cause uverwritten issu to over come that we using time nd date for multiples of using time
import os   # same as time date by using os we can over come by maping locations 
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.


def getFileName(request,filename):# creating a function to get the name of the file with corect tym nd dare nd store them in os path
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")#here calling correct datetime by using the datetime.now function and thas outcome is sting format(strftime)
    new_filename = "%s%s"%(now_time,filename) #creating the new file name in str format bt geting now_time and file name arug
    return os.path.join('uploads/',new_filename)# the new file is added in the uplods folder which is inside the os path
    
class category(models.Model):# create a class by inheriting the model inside tha db models ,,clss it creates the db tables by using the given class attrb
    name=models.CharField(max_length=150,null=False,blank=False) # category products names
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)#image is uploded in the  getFile name func above created 
   
    description=models.TextField(max_length=700,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")#default false means its dhowing so help txt makes 0 to show 1 for  hidden
    created_at=models.DateTimeField(auto_now_add=True) 
    
    def __str__(self): #this functions returns the name inside the category
        return self.name
    
     

class products(models.Model):# create a class by inheriting the model inside tha db models ,,clss it creates the db tables by using the given class attrb
    category = models.ForeignKey(category,on_delete=models.CASCADE)#here the category is joinin with the products query ,(the category prim key is foreign key for products)
    name=models.CharField(max_length=150,null=False,blank=False) #  products names
    vendor=models.CharField(max_length=150,null=False,blank=False) # products  vendor names
    product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)#image is uploded in the  getFile name func above created 
    product_image1=models.ImageField(upload_to=getFileName,null=True,blank=True)
    product_image2=models.ImageField(upload_to=getFileName,null=True,blank=True)
    product_image3=models.ImageField(upload_to=getFileName,null=True,blank=True)
    quantity=models.IntegerField(null=False,blank=False)
    orginal_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=700,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")#default false means its dhowing so help txt makes 0 to show 1 for  hidden
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True) 
    slug = models.SlugField(unique=True  , null=True , blank=True)
    
    
    def __str__(self): #this functions returns the name inside the category
        return self.name
    
    
    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(products ,self).save(*args , **kwargs)


    
"""   
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid = models.BooleanField(default = False)
    
    
    
class CartItems(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(products,on_delete=models.SET_NULL,null=True,blank = True)
    quantity = models.PositiveIntegerField(default=0)
"""
    
 
class CartItem(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.user.username

    
