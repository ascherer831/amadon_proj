from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process(request):
    if request.method == 'POST':
        order_item = Product.objects.filter(id=request.POST['id'])
        order_quant = int(request.POST['quantity'])
        item_price = float(order_item[0].price)
        order_total = item_price * order_quant
        Order.objects.create(quantity_ordered = order_quant, total_price = order_total)
        return redirect('/checkout')
    else:
        return redirect('/')
        

# def checkout(request):
#     current_order = Order.objects.last()
#     item_quant = current_order['quantity']
#     price_from_form = float(request.POST["price"])
#     total_charge = quantity_from_form * price_from_form
#     all_orders_quant = 0
#     all_orders_price = 0
#     orders = Order.objects.all()
#     for order in orders:
#         all_orders_quant += order['quantity_ordered']
#         all_orders_price += order['total_price']
#     context = {
#         "all_orders": Order.objects.all(),
#         "all_price": all_orders_price,
#         "all_quant": all_orders_quant
#     }
#     print("Charging credit card...")
#     return render(request, "store/checkout.html", context)
def checkout(request):
    total_spent = 0
    total_items = 0
    orders = Order.objects.all()

    for order in orders:
        total_spent += order.total_price
        total_items += order.quantity_ordered
    
        context = {
        "current_order": Order.objects.last(),
        "total_spent": total_spent,
        "total_items": total_items,
    }

    return render(request, "store/checkout.html", context)