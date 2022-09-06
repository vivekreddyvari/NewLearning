# Imports
import json
from datetime import datetime
import sys, traceback
from logging import Logger
from http import HTTPStatus

# Project Description
"""

Suppose we have a widget online sales application and we are writing backend for it, we want a base
WidgetException class that we will use as the base class for all our custom exceptions we raise from
our Widget application

Further we have determined that we will need the following categories of exceptions.

1. Supplier Exceptions
    a. Not Manufactured anymore
    b. Production delayed
    c. Shipping delayed
2. Checkout Exceptions
    a. Inventory type exceptions
        - out of stock
    b. Pricing Exceptions
        - Invalid Coupon Code
        - Cannot stack coupons

Coding:
    Steps:
    Write an exception class hirerachy to capture this, In addition, we would like to implement
    the following functionality.
    - implement separate internal error message and user error message
    - implement an http status code associated to each exception type (keep it simple, use a 500 (server error)
    error for everything except invalid coupon code, and cannot stack coupons, these can be 400 (bad request)
    - implement a logging function that can be called to log the exception details, time it occurred etc
    - implement a function that can be called to produce a json string the exception details you want to display
    to your user (include http status code) e.g. 400 the user error message. etc

Bonus:
log the traceback you'll have to do a bit research of that
Use the TraceBackException class in the traceback module.

"""


class Sales:
    """Sales details"""
    def __init__(self, sales_id, sales_type):
        self.sales_id = sales_id
        self.sales_type = sales_type


class WidgetException(Exception):
    """ Base Widget Exception """
    message = "Generic Widget Exception "
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, *args, customer_message=None):
        super().__init__(*args)
        if args:
            self.message = args[0]
        self.customer_message = customer_message if customer_message is not None else self.message

    @property
    def traceback(self):
        return traceback.TracebackException.from_exception(self).format()

    def log_exception(self):
        exception = {
            "type": type(self).__name__,
            "http_status": self.http_status,
            "message": self.args[0] if self.args else self.message,
            "args": self.args[1:],
            "traceback": list(self.traceback)
        }
        print(f"Exception: {datetime.utcnow().isoformat()}:{exception}")

    def to_json(self):
        response = {
            'code': self.http_status.value,
            'message': '{}: {}'.format(self.http_status.phrase, self.customer_message),
            'category': type(self).__name__,
            'time_utc': datetime.utcnow().isoformat()
        }
        return json.dumps(response)

# Testing
try:
    raise WidgetException('custom message', 10, 100)
except WidgetException as ex:
    ex.log_exception()
    print(ex.to_json())

try:
    raise WidgetException(customer_message='A custom message')
except WidgetException as ex:
    ex.log_exception()
    print(ex.to_json())


class SupplierException(WidgetException):
    """ Indicates Supplier exception has occurred (not user caused) """
    message = 'Supplier Exception'
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR


class NotManufacturedException(SupplierException):
    """ Indicates Not Manufactured exception"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "Widget is no longer Manufactured by supplier"


class ProductDelayedException(SupplierException):
    """ Indicates Product delayed exception"""
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "Widget is delayed by manufacturer "


class ShippingDelayedException(SupplierException):
    """" Indicates Shipping is delayed """
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "Widget shipping delayed by supplier "


class CheckoutException(WidgetException):
    """ Indicates checkout exception has occurred """
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "Widget Checkout Exception"


class InventoryTypeException(CheckoutException):
    """ Indicates checkout exception has occurred """
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "Checkout Inventory Exception"


class OutOfStockException(InventoryTypeException):
    """ Indicates Out of stock for the widget """
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "Item/Inventory Out of Stock Exception"


class PricingException(CheckoutException):
    """ Indicates pricing exceptions has occurred 5xx Type Error """
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "Checkout Pricing Exception "


class InvalidCouponCodeException(PricingException):
    """Indicates Invalid coupon Code """
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "Invalid checkout coupon code Exception"


class CannotStackCouponException(PricingException):
    """ Indicates Cannot stack coupon Exception """
    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    message = "Cannot stack checkout Coupon code "


try:
    raise CannotStackCouponException()
except CannotStackCouponException as ex:
    ex.log_exception()
    print(ex.to_json())


e = InvalidCouponCodeException(
    'User tried to pull a fast one on us', customer_message='Sorry, this coupon is not valid'
)
print(e.log_exception())

print('\n\n\n')

print(e.to_json())

