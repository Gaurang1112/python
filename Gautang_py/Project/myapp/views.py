from django.shortcuts import render,redirect
from .models import User,Contact,Product,Wishlist
import requests
import random

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            message=request.POST['message'],
    
        )
        msg="Contact Saved Successfully"
        return render(request,'contact.html',{'msg':msg})
    else:   
        return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def cart(request):
    return render(request,'cart.html')

def category(request):
    products=Product.objects.all()
    return render(request,'category.html',{'products':products})

def confirmation(request):
    return render(request,'confirmation.html')

def elements(request):
    return render(request,'elements.html')

def login(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                if user.usertype=="buyer":
                    request.session['email']=user.email
                    request.session['fname']=user.fname
                    return render(request,'index.html')
                else:
                    request.session['email']=user.email
                    request.session['fname']=user.fname
                    return render(request,'seller-index.html')
                    
            else:
                msg="Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        except:
            msg="Email Not Registered"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        return render(request,'login.html')
    except:
        return render(request,'login.html')

def single_blog(request):
    return render(request,'single-blog.html')

def single_product(request):
    return render(request,'single-product.html')

def tracking(request):
    return render(request,'tracking.html')

def checkout(request):
    return render(request,'checkout.html')

def signup(request):
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg="Email Already Registered"
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                        fname=request.POST['fname'],
                        lname=request.POST['lname'],
                        email=request.POST['email'],
                        mobile=request.POST['mobile'],
                        address=request.POST['address'],
                        password=request.POST['password'],
                        usertype=request.POST['usertype'],
                )
            msg="User Registered Successfully"
            return render(request,'signup.html',{'msg':msg})
        else:
            msg="Password & Confirm Password Does Not Matched"
            return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')

def change_password(request):
    if request.method=="POST":
        user=User.objects.get(email=request.session['email'])
        if user.password==request.POST['old_password']:
            if request.POST['new_password']==request.POST['cnew_password']:
                user.password=request.POST['new_password']
                user.save()
                return redirect('logout')
            else:
                msg="New Password & Confirm New Password Does Not Matched"
                return render(request,'change-password.html',{'msg':msg})
        else:
            msg="Old Password Does Not Matched"
            return render(request,'change-password.html',{'msg':msg})
    else:
        return render(request,'change-password.html')

def forgot_password(request):
    if request.method=="POST":
        try:
            mobile=request.POST['mobile']
            User.objects.get(mobile=mobile)
            url = "https://www.fast2sms.com/dev/bulkV2"
            otp=random.randint(1000,9999)
            querystring = {"authorization":"q5aBNsmTPnWZ7KfvortRpQli6C2LXE8FuwHhDzOUYAS1kcI9eMBEcIUTmaxOK5tzFfSL8pe2rlP4Z3G6","variables_values":str(otp),"route":"otp","numbers":str(mobile)}
            headers = {'cache-control': "no-cache"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
            return render(request,'otp.html',{'mobile':mobile,'otp':otp})
        except Exception as e:
            print(e)
            msg="Mobile Number Not Registered"
            return render(request,'forgot-password.html',{'msg':msg}) 
    else:
        return render(request,'forgot-password.html') 

def verify_otp(request):
    mobile=request.POST['mobile']
    otp=request.POST['otp']
    uotp=request.POST['uotp']

    if otp==uotp:
        return render(request,'new-password.html',{'mobile':mobile})
    else:
        msg="Invalid OTP"
        return render(request,otp.html,{'mobile':mobile,'otp':otp,'msg':msg})
    
def new_password(request):
    mobile=request.POST['mobile']
    np=request.POST['new_password']
    cnp=request.POST['cnew_password']

    if np==cnp:
        user=User.objects.get(mobile=mobile)
        user.password==np
        user.save()
        msg="Password Updated Successfully"
        return render(request,'login.html',{'msg':msg})
    else:
        msg="Password & Confirm Password Does Not Matched"
        return render(request,'new-password.html',{'mobile':mobile,'msg':msg})
    
def seller_add_product(request):
        seller=User.objects.get(email=request.session['email'])
        if request.method=="POST":
            Product.objects.create(
                seller=seller,
                product_brand=request.POST['product_brand'],
                product_price=request.POST['product_price'],
                product_size=request.POST['product_size'],
                product_pic=request.FILES['product_pic'],
            )
            msg="Product Added Successfuly"
            return render(request,'seller-add-product.html',{'msg':msg})
        else:
            return render(request,'seller-add-product.html')
        
def seller_view_product(request):
    seller=User.objects.get(email=request.session['email'])
    products=Product.objects.filter(seller=seller)
    return render(request,'seller-view-product.html',{'products':products})

def seller_product_details(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'seller-product-details.html',{'product':product})

def product_details(request,pk):
    wishlist_flag=False
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    try:
        Wishlist.object.get(user=user,product=product)
        wishlist_flag=True
    except:
        pass
    return render(request,'product-details.html',{'product':product,'wishlist_flag':wishlist_flag})


def seller_edit_product(request,pk):
    product=Product.objects.get(pk=pk)
    if request.method=="POST":
        product.product_brand=request.POST['product_brand']
        product.product_price=request.POST['product_price']
        product.product_size=request.POST['product_size']
        try:
            product.product_pic=request.FILES['product_pic']
        except:
            pass
        product.save()
        msg="Product Saved Successfully"
        return render(request,'seller-edit-product.html',{'product':product,'msg':msg})
    else:
        return render(request,'seller-edit-product.html',{'product':product})
    
def seller_delete_product(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect('seller-view-product')

def seller_index(request):
    return request(request,'seller-index.html')

def add_to_wishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Wishlist.objects.create(user=user,product=product)
    return redirect('wishlist')

def wishlist(request):
    user=User.objects.get(email=request.session['email'])
    wishlists=Wishlist.objects.filter(user=user)
    return render(request,'wishlist.html',{'wishlists':wishlists})

def remove_from_wishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    wishlist=Wishlist.objects.get(user=user,product=product)
    wishlist.delete()
    return redirect('wishlist')