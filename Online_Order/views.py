from django.shortcuts import render
from .models import Restaurant, MenuItem, Order

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})

def menu_list(request, restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    menu_items = MenuItem.objects.filter(restaurant=restaurant)
    return render(request, 'menu_list.html', {'restaurant': restaurant, 'menu_items': menu_items})

def place_order(request, restaurant_id):
    if request.method == 'POST':
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        order = Order.objects.create(restaurant=restaurant, total_price=0)
        for item_id, quantity in request.POST.items():
            if item_id.startswith('item_'):
                item_id = int(item_id.replace('item_', ''))
                item = MenuItem.objects.get(pk=item_id)
                OrderItem.objects.create(order=order, item=item, quantity=quantity)
                order.total_price += item.price * int(quantity)
        order.save()
        return render(request, 'order_confirmation.html', {'order': order})
    else:
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        menu_items = MenuItem.objects.filter(restaurant=restaurant)
        return render(request, 'place_order.html', {'restaurant': restaurant, 'menu_items': menu_items})
