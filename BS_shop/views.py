from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect

from .models import *      #import all from modesls.py 
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .utils  import TokenGenerator,generate_token
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.views.generic import View
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def main(request):  # main page view functions 
    Category=category.objects.filter(status = 0)# filtering all the objects in category model(class)"status = o (which means avaliable categories is 0)"
    Products = products.objects.filter(category = 4)
    topdeals = products.objects.filter(category = 5)
        
    context = {
        "Products":Products,
        "Topdeals":topdeals,
        "Category":Category
        }
    
    return render(request,"main.html",context,)  #here passing the Category  parameter 
   
def nav(request):   # nav bar view functions
    return render(request,"navbar.html")

def catg(request):   # categories page view functions
    Category=category.objects.filter(status = 0) # filtering all the objects in category model(class)"status = o (which means avaliable categories is 0)"
    return render(request,"categories.html",{"Category":Category})  #here passing the Category  parameter 

   
    
def slider(request): #silder functions displayed in main page
        Products = products.objects.filter(category = 4) 
        topdeals = products.objects.filter(category = 5)
        
        context = {
            "Products":Products,
            "Topdeals":topdeals
        } 
        return render(request,"slider.html",context) 
    

def prods(request,Name): # in this func we using two parameters one is used to filter category name to disply in urls of produt page which means we are getting he name from categ and passing to url<str:name> 
     if(category.objects.filter(name = Name,status = 0)): # this condition is used to filtering the category status i.e avaliable aren't and name,if the name of categry is equals to the parameter we passing the condition satisfys nd goes to nxt step
        Products=products.objects.filter(category__name= Name) #if the above condition satisfies,storing the Products in products variable like filtering the objects from products by its category_name and its euals to  parameter name i.e both the category name and products category name matches
        return render(request,"product.html",{"Products":Products,"category__name":Name})  #here passing the product  parameter and passed parameter is used to fetch any kind of data directly from the data models to the html....  after we storing the category name as parameter we passing retun to the product page 
     
     
     else:
        messages.warning(request,"No Such Category Found")
        return redirect("main.html")
  
 

def single_product(request,cName,pName): #in this func we using two parameters one is used to filter category name another one is to disply particular product to disply in urls of single produt page which means we are getting the name from product and passing to url<str:categname> <str:particular prod name>
     pid = products.objects.filter(id = 8)
     topdeals = products.objects.filter(category = 3 ) #filtering the 3rd category from category model
     if(category.objects.filter(name = cName,status = 0)): #filtering category and the name is equals to cname in html template
         if(products.objects.filter(name = pName,status = 0)): #filtering product name and the name is equals to pname in html template
            singprod = products.objects.filter(name=pName,status = 0).first() #filtering 
            
            return render(request,"productsdetails.html",{"Singleprod":singprod,"fashion":topdeals,"productname":pName,"pid":pid," catname": cName,}) 
        
         else:
             messages.error(request,"no such Category Found")
             return redirect("catgpage")
             
         

     else:
        messages.warning(request,"No Such Category Found")
        return redirect("catgpage")
        
        
      
def registration(request):
    print("running sucessfuly")
    if request.method=="POST": #assuming the method is post
        usrname = request.POST['usname'] # it stores posting  datas from user in a variables,the post datas taken by variables from their input names the user were posts
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        
        
        
        if User.objects.filter(username = usrname): # here we alredy got the posted data from user and stored them in database now filtering the stored username and combining with the user posting usrname 
            messages.warning(request,"Username already exist! Please try some other name")
            return render(request,"user_details/register.html")
          
        # length of the usrname 
        if len(usrname)>15:
            messages.warning(request,"Username must be under 15 characters")
            return render(request,"user_details/register.html")
          
        # password match
        if password1 != password2:
            messages.warning(request,"Password incorrect")
            return render(request,"user_details/register.html")  
        
        # password character
        if len(password1)<6:
            messages.warning(request,"Password must be greater then 8 character")
            return render(request,"user_details/register.html") 
        
        if User.objects.filter(email = email): #here we alredy got the posted data from user and stored them in database now filtering the stored email and combining with the user posting email 
            messages.warning(request,"email already exists")
            return render(request,"user_details/register.html") # the waring occurs then it disply messages in register.html page
            
        
        user = User.objects.create_user(usrname,email,password1)#here we creating user database by storing the posted data variables by importing user module  and passing 3 arguments  
        user.is_active = False #user doesn't active until email verf
        user.save() # storing the user module in USER variable and save it

        email_subject = "Activate Your Account"
        mesages = render_to_string('user_details/activate.html',{ # render to string use to store data in a variables and pass them to html pages
        'user':user, #user name from user
        'domain':'127.0.0.1:8000', #domain 
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),   #taking primary key by encoding format it makes specified key for specified user
        'token':generate_token.make_token(user)#it generates specified token for specified user
        })
        email_message = EmailMessage(email_subject,mesages,settings.EMAIL_HOST_USER,[email]) # passing all contentes in email message format and store them in a variable 
        email_message.send()  # sending the email variable
        messages.success(request,"Activate Your Account  by clicking the link in your gamil")
        return render(request,"user_details/login.html") # all the datas collected and stored then it render to requested login page
             
    return render(request,"user_details/register.html") #all func are held in register page

class ActivateAccountView(View): #to actiate the account creating a token to decodeing the primary key (checking pk matches)
      def get(self,request,uidb64,token): # passing arguments pk uidb64 and token  are the two arug requested from url and get used in all classes
          try:# try for
              uid = force_str(urlsafe_base64_decode(uidb64)) #uid variable ==  force_str(urlsafe_base64_decode(uidb64)) from pk we already encoded
              user = User.objects.get(pk = uid) #here gets the user as users prm key uid
        
          except Exception as identifier:
              user = None
          if user is not None and generate_token.check_token(user,token): # if the user is not none then decode (check the token matches wit user variab aren't)
              user.is_active = True # the above user uid matches with the tokens when it encoded then users status is active
              user.save()
              messages.success(request,"Activated succesfully")
              return redirect('logs')
          return render(request,'user_details/activationfailed.html')
           

def signin(request):
    
     if request.method=="POST": #assuming the method is post
        usrname = request.POST['usname'] # it stores posting  datas from user in a variables,the post datas taken by variables from their input names the user were posts
        passworduser = request.POST['pass1']
        Myuser = authenticate(username = usrname,password = passworduser)
        
        if Myuser is not None:
            login(request,Myuser)
            messages.success(request,"Login Sucess")
            return redirect('mainpage')
           
        
        else:
            messages.error(request,"Invalid Credentials")
            return render(request,"user_details/login.html")
            
            
     return render(request,"user_details/login.html")
 
def logot(request):
    logout(request)
    return redirect("mainpage")


def add_to_cart(request,catName,proName,product_id,):
    pro = products.objects.filter(id = product_id)
    catname = category.objects.filter(name = catName,status = 0)
    podname = products.objects.filter(name = proName,status = 0)
    prodcts = products.objects.get(id = product_id)
    cartitem = CartItem.objects.all()
    

    context={ 
             "pro": pro,
             " catname": catname,
             "podname":podname ,
             "cartitem":cartitem,
             }
    cart_item,created = CartItem.objects.get_or_create(product= prodcts,user=request.user)
    cart_item.save()
    return render(request,"cart.html",context)

"""cart,_= Cart.objects.get_or_create(user = user, is_paid = False) 
   Cart_item = CartItems.objects.create(cart = cart,product = prodcts)"""
    