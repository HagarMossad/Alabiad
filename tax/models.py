from django.db import models

# Create your models here.
from home.models import TAXES_CODES , TAX_SUBTYPE

class TaxTotals (models.Model):
    taxType = models.CharField(max_length=250,choices=TAXES_CODES )
    amount = models.DecimalField(decimal_places=5 ,max_digits=100 )
    parent_id = models.CharField(max_length=250 , null=True , blank=True)
    parent_type = models.CharField(max_length=250 , null=True , blank=True)


class taxableItems(models.Model):
    taxType = models.CharField(max_length= 250,choices=TAXES_CODES)
    amount = models.DecimalField(decimal_places= 5 , max_digits=100  , null=True , blank=True)
    subType =  models.CharField(max_length= 250 ,choices=TAX_SUBTYPE)
    rate = models.DecimalField(decimal_places= 5 , max_digits=100 ,null=True ,blank=True)
    parent_id = models.CharField(max_length=250 , null=True , blank=True)
    parent_type = models.CharField(max_length=250 , null=True , blank=True)

TAX_STAUS = [
    ('Active' , "Active"),
    ('Not Active' , "Not Active")
]
class TaXCategory(models.Model):
    name = models.CharField(max_length= 250 ,blank=True , null=True )
    validFrom = models.DateField(auto_now= False , blank=True , null=True)
    validTo   = models.DateField(auto_now= False , blank=True , null=True)
    status = models.CharField(max_length=250 , default="Active" , choices=TAX_STAUS )
    tax_table = models.ManyToManyField(taxableItems ,blank=True , null=True)
    def __str__(self):
        return str(self.name)