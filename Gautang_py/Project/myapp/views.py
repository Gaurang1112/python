from django.shortcuts import render,redirect
from .models import User

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def cart(request):
    return render(request,'cart.html')

def category(request):
    return render(request,'category.html')

def confirmation(request):
    return render(request,'confirmation.html')

def elements(request):
    return render(request,'elements.html')

def login(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session['email']=user.email
                request.session['fname']=user.fname
                return render(request,'index.html')
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
    return render(request,'forgot-password.html') 
    