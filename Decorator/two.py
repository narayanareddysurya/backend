# Decorator

 #what is decorator?
 #Decorator is function, it taken function as argunment, and return modified function



 def login_req(func):
     def inner(name, flag):
       if flag != True:
        print("login required! please login")
    else:
        return func(name,flag)
    
  return inner
 
 def home_page(name,flag):
     print("welocme to home page")
     
     
 @login_req
  def order_page(name,flag):
   print("profile page")
   
   def product_page(name,flag):
       print("product page")
       
    home_page("rahul", true)
    product_page("rahul",true)
    #for accessing profile page and order page - login required
    profile_page("rahul", true)
    order_page("rahul",true)
    