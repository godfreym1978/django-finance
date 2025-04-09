
# Create your views here.

# mybackendapp/views.py
from django.shortcuts import render
from django.apps import apps
from .models import Amex61001Dtl, AmexCorpDtl, AmexCostcoDtl, AmexPrsnlSvg, BoaBankDtl, BoaVisaDtl, ChaseBankChk, ChaseBankSvr, ChaseRentChk, ChaseRentChk, ChaseBankSvr, ChaseVisaDtl, CommbankChkDtl, CommbankSvrDtl, FiaAmexDtl, FidelityBankDtl, FidelityMfTbl, FifthrdBankDtl, HdfcBankDtl, IciciBankDtl, MutualFundInv, RothWf401, SuntrustBankDtl, UsaStockTbl, WellsFargoVisaDtl # Replace with your model names.

import sys
print(sys.path)

'''
Commented out to create dynamic views and templates
def amex61001_dtl_view(request):
    data = Amex61001Dtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/Amex61001Dtl.html", {"data": data})

def amexcorp_dtl_view(request):
    data = AmexCorpDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/AmexCorpDtl.html", {"data": data})

def amexcostco_dtl_view(request):
    data = AmexCostcoDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/AmexCostcoDtl.html", {"data": data})    

def amexprsnlsvg_dtl_view(request):
    data = AmexPrsnlSvg.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/AmexPrsnlSvg.html", {"data": data})

def boabankchk_dtl_view(request):
    data = BoaBankDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/BoaBankDtl.html", {"data": data})

def boabankvisa_dtl_view(request):
    data = BoaVisaDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/BoaVisaDtl.html", {"data": data})

def chasechk_dtl_view(request):
    data = ChaseBankChk.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/ChaseBankChk.html", {"data": data})

def chasesvr_dtl_view(request):
    data = ChaseBankSvr.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/ChaseBankSvr.html", {"data": data})

def chaserent_dtl_view(request):
    data = ChaseRentChk.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/ChaseRentChk.html", {"data": data})

def chasevisa_dtl_view(request):
    data = ChaseVisaDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/ChaseVisaDtl.html", {"data": data})

def commbankchk_dtl_view(request):
    data = CommbankChkDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/CommbankChkDtl.html", {"data": data})

def commbanksvr_dtl_view(request):
    data = CommbankSvrDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/CommbankSvrDtl.html", {"data": data})

def fiaamex_dtl_view(request):
    data = FiaAmexDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/FiaAmexDtl.html", {"data": data})

def fidbankdtl_dtl_view(request):
    data = FidelityBankDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/FidelityBankDtl.html", {"data": data})

def fidmftbl_dtl_view(request):
    data = FidelityMfTbl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/FidelityMfTbl.html", {"data": data})

def fifthbankdtl_dtl_view(request):
    data = FifthrdBankDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/FifthrdBankDtl.html", {"data": data})

def hdfcbank_dtl_view(request):
    data = HdfcBankDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/HdfcBankDtl.html", {"data": data})

def icicibank_dtl_view(request):
    data = IciciBankDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/IciciBankDtl.html", {"data": data})

def mfinv_dtl_view(request):
    data = MutualFundInv.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/MutualFundInv.html", {"data": data})

def roth401_dtl_view(request):
    data = RothWf401.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/RothWf401.html", {"data": data})

def suntrust_dtl_view(request):
    data = SuntrustBankDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/SuntrustBankDtl.html", {"data": data})

def usastock_dtl_view(request):
    data = UsaStockTbl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/UsaStockTbl.html", {"data": data})


def wfvisa_dtl_view(request):
    data = WellsFargoVisaDtl.objects.all()  # Retrieve all records from Table 1
    return render(request, "fin/WellsFargoVisaDtl.html", {"data": data})

'''

# fin/views.py
from django.shortcuts import render
from django.apps import apps

def dynamic_table_view(request, table_name):
    try:
        model = apps.get_model('fin', table_name)
        data = model.objects.all()

        fields = [field.name for field in model._meta.fields]

        context = {
            'table_name': table_name,
            'fields': fields,
            'data': data,
        }
        return render(request, 'dynamic_table.html', context)
    except LookupError:
        return render(request, 'table_not_found.html', {'table_name': table_name})