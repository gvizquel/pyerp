"""Modelos para la orden de venta
"""
# Librerias Django
from django.db import models

# Librerias de terceros
from apps.base.models import PyFather, PyProduct
from apps.sale.models import PySaleOrder


# ========================================================================== #
class PySaleOrderDetail(PyFather):
    """Modelo del detalle de la orden de pago
    """
    sale_order = models.ForeignKey(
        PySaleOrder,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        PyProduct,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    description = models.TextField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    """Pendientes estos dos modelos por incluir no se donde
    """
    # measure_unit = models.ForeignKey(
    #     PyMesureUnit,
    #     null=True,
    #     blank=True,
    #     on_delete=models.CASCADE
    # )
    # product_tax = models.ForeignKey(
    #     PyProductTax,
    #     null=True,
    #     blank=True,
    #     on_delete=models.CASCADE
    # )
    amount_untaxed = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    amount_taxt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amount_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['sale_order', 'product'],
                name='product_order_unique'
            )
        ]
