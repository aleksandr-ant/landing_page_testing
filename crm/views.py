from django.shortcuts import render

from cms.models import CmsSlider
from crm.forms import OrderForm
from crm.models import Order
from price.models import PriceCard, PriceTable


def home_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    dict_obj = {
        'slider_list': slider_list,
        'pk_1': pc_1,
        'pk_2': pc_2,
        'pk_3': pc_3,
        'price_table': price_table
    }
    return render(request, 'index.html', dict_obj)


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name=name, order_phone=phone)
    element.save()
    return render(request, 'thanks.html', {
        'name': name,
        'phone': phone
    })
