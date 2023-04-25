from django.shortcuts import render, redirect
from .models import Food , Cart
from django.db.models import Q

# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json




def food(request):
    foods = Food.objects.all()
    total_item = Cart.objects.all().count()
    context = {'foods': foods, 'total_item': total_item}
    return render(request, 'index.html', context)


def food_details(request, pk):
    total_item=0
    food = Food.objects.get(pk=pk)
    item_already_in_cart = False
    
    # count the number of items in the cart with the same food_id
    total_item = Cart.objects.filter(food_id=pk).count()
    
    context = {'foods': food, 'item_already_in_cart': item_already_in_cart, 'total_item': total_item}
    return render(request, 'food-detail.html', context)


def add_to_cart(request):
    food_id = request.GET.get('food_id')
    food_name = Food.objects.get(id=food_id)
    food = Food.objects.filter(id=food_id)
    cart_item = Cart.objects.filter(food_id=food_id).first()
    
    if cart_item: # if item already exists in cart, increment its quantity
        cart_item.quantity += 1
        cart_item.save()
    else: # if item doesn't exist in cart, add it as a new item
        for f in food:
            image = f.image
            price = f.price
            Cart(food=food_name, image=image, price=price).save()

    # update the total_item count
    total_item = Cart.objects.filter(food_id=food_id).count()
    
    return redirect(f"/food-detail/{food_id}")

def show_cart(request):
    cart_items = Cart.objects.all()
    total_price = sum(item.total() for item in cart_items)
    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'show_cart.html', context)

def remove_cart(request, cart_item_id):
    cart_item = Cart.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('show_cart')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')

