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
    path('signup/',views.signup,name='signup')

   
]