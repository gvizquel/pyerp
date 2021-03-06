"""Modelos para la orden de venta
"""
# Librerias Django
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

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


# ========================================================================== #
@receiver(post_save, sender=PySaleOrderDetail)
def post_save_sale_order(sender, instance, created, **kwargs):
    _sale_order = PySaleOrder.objects.get(pk=instance.sale_order.pk)
    _amount_untaxec = sender.objects.filter(sale_order=instance.sale_order.pk).aggregate(Sum('amount_total'))
    _sale_order.amount_untaxec = _amount_untaxec['amount_total__sum']
    _sale_order.save()


# ========================================================================== #
@receiver(post_delete, sender=PySaleOrderDetail)
def post_delete_sale_order(sender, instance, **kwargs):
    _sale_order = PySaleOrder.objects.get(pk=instance.sale_order.pk)
    _amount_untaxec = sender.objects.filter(sale_order=instance.sale_order.pk).aggregate(Sum('amount_total'))
    _sale_order.amount_untaxec = _amount_untaxec['amount_total__sum']
    _sale_order.save()
