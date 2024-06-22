# backend/accounting_service/matching.py
from .models import Order
from sqlalchemy import and_

def match_orders():
    matches = []
    buy_orders = Order.query.filter_by(order_type='buy', status='open').all()
    sell_orders = Order.query.filter_by(order_type='sell', status='open').all()

    for buy_order in buy_orders:
        for sell_order in sell_orders:
            if (
                buy_order.product_details['brand'] == sell_order.product_details['brand'] and
                buy_order.product_details['model'] == sell_order.product_details['model'] and
                buy_order.product_details['condition'] == sell_order.product_details['condition'] and
                buy_order.price >= sell_order.price
            ):
                matches.append((buy_order, sell_order))
                # Update order status to 'matched'
                buy_order.status = 'matched'
                sell_order.status = 'matched'
                break  # Stop after finding the first match for this buy order

    return matches
