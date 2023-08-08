from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('page/',views.page,name='page'),
    path('about/',views.about,name='about'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('news/',views.news,name='news'),
    path('shop/',views.shop,name='shop'),
    path('single-news/',views.single_news,name='single-news'),
    path('account/',views.account,name='account'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
]