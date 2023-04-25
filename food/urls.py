from django.urls import path
from . import views

urlpatterns=[
    
    path('index/',views.food, name='index'),
    path('home/',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('food-detail/<int:pk>',views.food_details, name='food-detail'),
    path('addtocart/',views.add_to_cart, name='addtocart'),
    path('show_cart',views.show_cart,name='show_cart'),
    path('remove_cart/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    

]