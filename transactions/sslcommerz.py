import string
import random
from django.conf import settings
from sslcommerz_lib import SSLCOMMERZ
from .models import PaymentGateway



def generator_trangection_id( size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


    

def sslcommerz_payment_gateway(request, name, amount):
 
    gateway = PaymentGateway.objects.all().first()
    cradentials = {'store_id': gateway.store_id,
            'store_pass': gateway.store_pass, 'issandbox': True} 
            
    sslcommez = SSLCOMMERZ(cradentials)
    body = {}
    body['total_amount'] = amount
    body['currency'] = "BDT"
    body['tran_id'] = generator_trangection_id()
    body['success_url'] = 'http://localhost:8000/payment/success/'
    body['fail_url'] = 'http://localhost:8000/payment/payment/faild/'
    body['cancel_url'] = 'http://localhost:8000/payment'
    body['emi_option'] = 0
    body['cus_name'] = name
    body['cus_email'] = 'request.data["email"]'
    body['cus_phone'] = 'request.data["phone"]'
    body['cus_add1'] = 'request.data["address"]'
    body['cus_city'] = 'request.data["address"]'
    body['cus_country'] = 'Bangladesh'
    body['shipping_method'] = "NO"
    body['multi_card_name'] = ""
    body['num_of_item'] = 1
    body['product_name'] = "Test"
    body['product_category'] = "Test Category"
    body['product_profile'] = "general"
    body['value_a'] = name

    response = sslcommez.createSession(body)
    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]