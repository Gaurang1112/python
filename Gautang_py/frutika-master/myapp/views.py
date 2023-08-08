from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def page(request):
    return render(request,'page.html')

def about(request):
    return render(request,'about.html')

def cart(request):
    return render(request,'cart.html')

def checkout(request):
    return render(request,'checkout.html')

def news(request):
    return render(request,'news.html')

def shop(request):
    return render(request,'shop.html')

def single_news(request):
    return render(request,'single-news.html')

def account(request):
    return render(request,'account.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

