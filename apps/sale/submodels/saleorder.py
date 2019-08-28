"""Modelos para la orden de venta
"""
# Librerias Django
from django.db import models

# Librerias de terceros
from apps.base.models import PyFather, PyPartner

SALE_STATE = (
        ("draft", "Borrador"),
        ('open', 'Consumible'),
        ('cancel', 'Servicio'),
        ('confirmada', 'confirmada')
    )


# ========================================================================== #
class PySaleOrder(PyFather):
    """Modelo de la orden de pago
    """
    name = models.CharField('Nombre', max_length=80)
    partner_id = models.ForeignKey(
        PyPartner,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    date_order = models.DateTimeField(auto_now_add=True, null=True)
    amount_untaxec = models.DecimalField(
        'Monto Neto',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    amount_taxt = models.DecimalField(
        'Total Impuestos',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    amount_total = models.DecimalField(
        'Total',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    description = models.TextField(blank=True, null=True)
    state = models.CharField(
        choices=SALE_STATE,
        max_length=64,
        default='draft'
    )
