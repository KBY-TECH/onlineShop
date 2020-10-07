from django.urls import path
from .views import *

app_name = 'order'

urlpatterns = [
    path('create/', orderCreate, name='order_create'),
    path('create_ajax/', orderCreate_Ajax.as_view(), name='order_create_ajax'),
    path('checkout/', OrderCheckoutAjaxView.as_view(), name='order_checkout'),
    path('validation/', OrderImpAjaxView.as_view(), name='order_validation'),
    path('complete/', orderComplete, name='order_complete'),
]