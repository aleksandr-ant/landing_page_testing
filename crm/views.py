from django.shortcuts import render
from crm.forms import OrderForm
from crm.models import Order


def home_page(request):
    form = OrderForm()
    order_list = Order.objects.all()
    return render(request, 'home.html', {'order': order_list, 'form': form})


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, 'thanks_page.html', {
        'name': name,
        'phone': phone
    })
