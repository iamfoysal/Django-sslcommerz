
from django.urls import path
from .views import *

app_name = "transactions"

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('transaction/', DonateView, name='transaction'),
    path('payment/success/', CheckoutSuccessView.as_view(), name='success'),
    path('payment/faild/', CheckoutFaildView.as_view(), name='faild'),

]
