# mybackendapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
   path('Amex61001Dtl.html', views.amex61001_dtl_view, name='view_Amex61001Dtl_data'), # Corrected to match URL
   path('AmexCorpDtl.html', views.amexcorp_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL

   
   path('AmexCostcoDtl.html', views.amexcostco_dtl_view, name='view_AmexCostcoDtl_data'), # Corrected to match URL
   
   path('AmexPrsnlSvgDtl.html', views.amexprsnlsvg_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('BoaBankDtl.html', views.boabankchk_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('BoaVisaDtl.html', views.boabankvisa_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('ChaseBankChk.html', views.chasechk_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('ChaseRentSvr.html', views.chasesvr_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('ChaseRentChk.html', views.chaserent_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('ChaseVisaDtl.html', views.chasevisa_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('CommbankChkDtl.html', views.commbankchk_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL

   path('CommbankSvrDtl.html', views.commbanksvr_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('FiaAmexDtl.html', views.fiaamex_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('FidelityBankDtl.html', views.fidbankdtl_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('FidelityMfTbl.html', views.fidmftbl_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('FifthrdBankDtl.html', views.fifthbankdtl_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('HdfcBankDtl.html', views.hdfcbank_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('IciciBankDtl.html', views.icicibank_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('MutualFundInv.html', views.mfinv_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('RothWf401.html', views.roth401_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('SuntrustBankDtl.html', views.suntrust_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('UsaStockTbl.html', views.usastock_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
   path('WellsFargoVisaDtl.html', views.wfvisa_dtl_view, name='view_AmexCorpDtl_data'), # Corrected to match URL
]