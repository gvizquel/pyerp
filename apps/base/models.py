"""Modelos del modulo
"""
# Librerias Standard
from datetime import datetime, timedelta

# Librerias Django
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.timesince import timesince
from django.utils.translation import ugettext_lazy as _

# Librerias en carpetas locales
from .submodels.base_config import BaseConfig
from .submodels.company import PyCompany
from .submodels.cron import PyCron
# from .submodels/father.py import *
# from submodels/model2.py import *
from .submodels.father import PyFather
from .submodels.locations import PyComuna, PyCountry, PyRegion
from .submodels.log import PyLog
from .submodels.partner import PyPartner
from .submodels.product import PyProduct
from .submodels.product_category import PyProductCategory
from .submodels.product_webcategory import PyProductWebCategory
