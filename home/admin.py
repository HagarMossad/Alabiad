from django.contrib import admin
from .models import TaxableTypes , TaxSubtypes
# Register your models here.
admin.site.register(TaxSubtypes)
admin.site.register(TaxableTypes)