from django.urls import path
from . import views



urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('cart/',views.cart,name='cart'),
    path('category/',views.category,name='category'),
    path('confirmation/',views.confirmation,name='confirmation'),
    path('elements/',views.elements,name='elements'),
    path('login/',views.login,name='login'),
    path('single-blog/',views.single_blog,name='single-blog'),
    path('single-product/',views.single_product,name='single-product'),
    path('tracking/',views.tracking,name='tracking'),
    path('checkout/',views.checkout,name='checkout'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('change-password/',views.change_password,name='change-password'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password')


]