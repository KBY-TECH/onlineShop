from django.shortcuts import render,get_object_or_404
from .models import *
from cart.cart import Cart
from .forms import *

# Create your views here.
def orderCreate(request):
    cart=Cart(request)
    if request.method=='post':
        form=OrderCreateForm(request.POST)
        if form.is_valid():
            order=form.save()
            if cart.coupon:
                order.coupon=cart.coupon
                order.discount=cart.get_discount_total()
                order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request,'order/created.html', {'order': order})
    else:
        form=OrderCreateForm()
    return render(request,'order/create.html',{'cart':cart,

                                               'form':'form'})
#JS 동작하지 않는 환경에서도 주문은 가능해야 한다.
# 그래서 JS가 안되는 경우 모두 백단에서 처리하여야 한다.

def orderComplete(request):
    order_id=request.GET.get('order_id')
    order=get_object_or_404(Order,id=order_id)
    return render(request,'order.created.html',{'order':order})

from django.views.generic.base import View
from django.http import JsonResponse

class orderCreate_Ajax(View):
    def post(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'authenticated':False},status=403)
        cart=Cart(request)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.get_discount_total()
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            data={
                "order_id":order.id
            }
            return JsonResponse(data)
        else:
            return JsonResponse({},status=401)