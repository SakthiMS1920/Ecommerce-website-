from django.urls import path
from .import views

urlpatterns = [
    path('',views.main,name="mainpage"), 
    #path('nav',views.nav,name="navigationpage"), 
    path('slid',views.slider,name="sliderpage"),
    path('collections',views.catg,name="catgpage"),
    path('collections/<str:Name>',views.prods,name="product"),#to fetch the category name we using <str:Name> the Name parrameter is from categories page  we allready fetched the categories name on main page fuc after that we finding tha products based on categories name nd passing it through the anchor link in catg page
    path('<str:cName>/<str:pName>',views.single_product,name="productdetails"),
    path('reg',views.registration,name="registration"),
    path('log',views.signin,name="logs"),
    path('logout',views.logot,name="logss"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name="activate"),#views.ActivateAccountView.as_view() is calling the class considering class as view and req for two arug
    path('<str:catName>,/<str:proName>,/<product_id>/',views.add_to_cart,name="cartt"),
]

    