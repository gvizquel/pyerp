# Librerias Django
from django.contrib import admin

# Librerias de terceros
from apps.base.models import (
    PyCompany, PyCountry, PyPartner, PyProduct, PyProductCategory)

admin.site.register(PyPartner)
admin.site.register(PyProduct)
admin.site.register(PyCountry)
admin.site.register(PyProductCategory)
admin.site.register(PyCompany)
