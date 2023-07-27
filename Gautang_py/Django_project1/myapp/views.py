from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            remarks=request.POST['remarks']
         )
        msg="Contact Saved Successfully"
        return render(request,'contact.html',{'msg':msg, 'contact':contact})
    else:    
        return render(request,'contact.html',{'contact':contact})

def signup(request):
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg="Email Already Registered"
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                    User.objects.create(
                        fanme=request.POST['fname'],
                        lanme=request.POST['lname'],
                        email=request.POST['email'],
                        mobile=request.POST['mobile'],
                        address=request.POST['address'],
                        gender=request.POST['gender'],
                        password=request.POST['password'],

                    )
                    msg="User Sign Up Successfully"
                    return render(request,'signup.html',{'msg':msg})
            else:
                msg="Password & Confirm Paassword Doed Not Matched"
                return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

