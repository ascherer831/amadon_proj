from django.shortcuts import render
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    total_charge = quantity_from_form * price_from_form
    all_orders_quant = 0
    all_orders_price = 0
    orders = { 'all_orders':Order.objects.all()}
    for order in Order.objects.all():
        all_orders_quant += order['quantity_ordered']
        all_orders_price += order['total_price']
    context = { 
        "all_orders": Order.objects.all(),
        "all_price": all_orders_price,
        "all_quant": all_orders_quant
    }
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return render(request, "store/checkout.html", context)