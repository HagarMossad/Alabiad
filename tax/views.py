from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import TaXCategory , taxableItems
from home.models import TAXES_CODES , TAX_SUBTYPE 

@login_required(login_url='login')
def taxes_list(request):
    taxes = TaXCategory.objects.all()
    page = "taxes_list.html"
    content = {
        'taxes' : taxes
    }
    return render(request , page, content)



def creat_tax (request) :
    if request.method=='POST' :
        tax= TaXCategory(
            name = request.POST.get('tax_name')
        )
        tax.save()
        return redirect ('tax_details' , tax.id)


def delete_tax(request , id ):
    TaXCategory.objects.get(id=id ).delete()
    return redirect('taxes_list')

@login_required(login_url='login')
def tax_details(request , id ):
    tax= TaXCategory.objects.filter(id = id).first()
    page = 'tax_details.html'
    taxe_codes = [{'val' : i[0] , 'text' : i[1] } 
                for i in TAXES_CODES]
    taxe_types = [{'val' : i[0] , 'text' : i[1] } 
                for i in TAX_SUBTYPE ]
    content = {
        'tax' :tax,
        'taxe_codes' : taxe_codes ,
        'taxe_types' : taxe_types 

        
    }

    if request.method == 'POST' :
        taxe_table = taxableItems(
            taxType = request.POST.get('taxType') ,
            amount = float (request.POST.get('amount') or 0 ),
            subType = request.POST.get('suptype') ,
            rate = float (request.POST.get('rate') or 0 ),
            parent_id= tax.id

        )
        taxe_table.save()
        tax.tax_table.add(taxe_table)
        tax.save()
        return redirect('tax_details' , tax.id)

        
               
    return render (request ,page , content)


def delete_taxable_item(request , id):
    item = taxableItems.objects.get(id=id)
    tax_id = item.parent_id
    item.delete()
    return redirect ('tax_details' , tax_id)
