import requests
from config.settings import STRIPE_API_KEY


def create_obj_payment(product_name):
    headers = {'Authorization': f'Bearer {STRIPE_API_KEY}'}
    params = {'name': product_name}
    response = requests.post('https://api.stripe.com/v1/products', headers=headers, params=params)
    data = response.json()
    return data['id']


def create_obj_price(product_id, price):
    headers = {'Authorization': f'Bearer {STRIPE_API_KEY}'}
    params = {'product': product_id, 'currency': 'rub', 'unit_amount': int(price*100)}
    response = requests.post('https://api.stripe.com/v1/prices', headers=headers, params=params)
    data = response.json()
    return data['id']


def create_session_pay(price_id):
    headers = {'Authorization': f'Bearer {STRIPE_API_KEY}'}
    params = {'success_url': 'http://localhost:8000/user/payment/success/', 'line_items[0][price]': price_id, 'line_items[0][quantity]': 1, 'mode': 'payment'}
    response = requests.post('https://api.stripe.com/v1/checkout/sessions', headers=headers, params=params)
    data = response.json()
    return data['url']

