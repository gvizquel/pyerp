"""Vistas para el módulo sale
"""
# Librerias Django
from django.shortcuts import render

# Librerias en carpetas locales
from .subviews.saleorderadd import SaleOrderAddView
from .subviews.saleorderdelete import SaleOrderDeleteView
from .subviews.saleorderdetailadd import SaleOrderDetailAddView
from .subviews.saleorderdetaildelete import SaleOrderDetailDeleteView
from .subviews.saleorderdetailedit import SaleOrderDetailEditView
from .subviews.saleorderedit import SaleOrderEditView
from .subviews.saleorderlist import SaleOrderListView
