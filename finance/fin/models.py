# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Amex61001Dtl(models.Model):
    #pk = models.CompositePrimaryKey('A61001_DATE', 'A61001_DEPOSIT', 'A61001_WITH')
    a61001_date = models.DateField(db_column='A61001_DATE',  primary_key=True)  # Field name made lowercase.
    a61001_desc = models.CharField(db_column='A61001_DESC', max_length=150, blank=True, null=True)  # Field name made lowercase.
    a61001_deposit = models.DecimalField(db_column='A61001_DEPOSIT', max_digits=10, decimal_places=2 )  # Field name made lowercase.
    a61001_with = models.DecimalField(db_column='A61001_WITH', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-a61001_date'] #order the records from the table
        #create a index on the table
        #indexes = [
        #    models.Index(fields=['-publish']),
        #    ]
        managed = False
        db_table = 'AMEX_61001_DTL'
        unique_together = (('a61001_date', 'a61001_deposit', 'a61001_with'),)
        #database = 'finance'  # Add this line


#this goes in the views.py file
class AmexCorpDtl(models.Model):
    #pk = models.CompositePrimaryKey('ACORP_DATE', 'ACORP_BAL')
    acorp_date = models.DateField(db_column='ACORP_DATE',  primary_key=True)  # Field name made lowercase.
    acorp_desc = models.CharField(db_column='ACORP_DESC', max_length=150, blank=True, null=True)  # Field name made lowercase.
    acorp_deposit = models.DecimalField(db_column='ACORP_DEPOSIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    acorp_with = models.DecimalField(db_column='ACORP_WITH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    acorp_bal = models.DecimalField(db_column='ACORP_BAL', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-acorp_date']
        managed = False
        db_table = 'AMEX_CORP_DTL'
        unique_together = (('acorp_date', 'acorp_bal'),)

class AmexCostcoDtl(models.Model):
    #pk = models.CompositePrimaryKey('COSTCO_DATE', 'COSTCO_DESC', 'COSTCO_DEPOSIT', 'COSTCO_WITH')
    costco_date = models.DateField(db_column='COSTCO_DATE',  primary_key=True)  # Field name made lowercase.
    costco_desc = models.CharField(db_column='COSTCO_DESC', max_length=150)  # Field name made lowercase.
    costco_deposit = models.DecimalField(db_column='COSTCO_DEPOSIT', max_digits=10, decimal_places=2)  # Field name made lowercase.
    costco_with = models.DecimalField(db_column='COSTCO_WITH', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-costco_date']
        managed = False
        db_table = 'AMEX_COSTCO_DTL'
        unique_together = (('costco_date', 'costco_desc', 'costco_deposit', 'costco_with'),)


class AmexPrsnlSvg(models.Model):
    #pk = models.CompositePrimaryKey('APS_TRAN_DATE', 'APS_BAL')
    aps_tran_type = models.CharField(db_column='APS_TRAN_TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    aps_tran_date = models.DateField(db_column='APS_TRAN_DATE',  primary_key=True)  # Field name made lowercase.
    aps_tran_amt = models.DecimalField(db_column='APS_TRAN_AMT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    aps_bal = models.DecimalField(db_column='APS_BAL', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-aps_tran_date']
        managed = False
        db_table = 'AMEX_PRSNL_SVG'
        unique_together = (('aps_tran_date', 'aps_bal'),)

class BoaBankDtl(models.Model):
    #pk = models.CompositePrimaryKey('BBD_DATE', 'BBD_DESC', 'BBD_BAL')
    bbd_date = models.DateField(db_column='BBD_DATE',  primary_key=True)  # Field name made lowercase.
    bbd_desc = models.CharField(db_column='BBD_DESC', max_length=100)  # Field name made lowercase.
    bbd_deposit = models.DecimalField(db_column='BBD_DEPOSIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bbd_with = models.DecimalField(db_column='BBD_WITH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    bbd_bal = models.DecimalField(db_column='BBD_BAL', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-bbd_date']
        managed = False
        db_table = 'BOA_BANK_DTL'
        unique_together = (('bbd_date', 'bbd_desc', 'bbd_bal'), ('bbd_date', 'bbd_desc', 'bbd_bal'),)


class BoaVisaDtl(models.Model):
    #pk = models.CompositePrimaryKey('BVD_DATE', 'BVD_DESC', 'BVD_DEPOSIT', 'BVD_WITH')
    bvd_date = models.DateField(db_column='BVD_DATE',  primary_key=True)  # Field name made lowercase.
    bvd_desc = models.CharField(db_column='BVD_DESC', max_length=100)  # Field name made lowercase.
    bvd_deposit = models.DecimalField(db_column='BVD_DEPOSIT', max_digits=10, decimal_places=2)  # Field name made lowercase.
    bvd_with = models.DecimalField(db_column='BVD_WITH', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-bvd_date']
        managed = False
        db_table = 'BOA_VISA_DTL'
        unique_together = (('bvd_date', 'bvd_desc', 'bvd_deposit', 'bvd_with'), ('bvd_date', 'bvd_desc', 'bvd_deposit', 'bvd_with'),)


class ChaseBankChk(models.Model):
    #pk = models.CompositePrimaryKey('CBC_DATE', 'CBC_DESC', 'CBC_BAL')
    cbc_date = models.DateField(db_column='CBC_DATE',  primary_key=True)  # Field name made lowercase.
    cbc_num = models.CharField(db_column='CBC_NUM', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cbc_desc = models.CharField(db_column='CBC_DESC', max_length=100)  # Field name made lowercase.
    cbc_deposit = models.DecimalField(db_column='CBC_DEPOSIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbc_with = models.DecimalField(db_column='CBC_WITH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbc_bal = models.DecimalField(db_column='CBC_BAL', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-cbc_date']
        managed = False
        db_table = 'CHASE_BANK_CHK'
        unique_together = (('cbc_date', 'cbc_desc', 'cbc_bal'), ('cbc_date', 'cbc_desc', 'cbc_bal'),)


class ChaseBankSvr(models.Model):
    #pk = models.CompositePrimaryKey('CBS_DATE', 'CBS_DESC', 'CBS_BAL')
    cbs_date = models.DateField(db_column='CBS_DATE',  primary_key=True)  # Field name made lowercase.
    cbs_num = models.CharField(db_column='CBS_NUM', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cbs_desc = models.CharField(db_column='CBS_DESC', max_length=100)  # Field name made lowercase.
    cbs_deposit = models.DecimalField(db_column='CBS_DEPOSIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbs_with = models.DecimalField(db_column='CBS_WITH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbs_bal = models.DecimalField(db_column='CBS_BAL', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-cbs_date']
        managed = False
        db_table = 'CHASE_BANK_SVR'
        unique_together = (('cbs_date', 'cbs_desc', 'cbs_bal'), ('cbs_date', 'cbs_desc', 'cbs_bal'),)


class ChaseRentChk(models.Model):
    #pk = models.CompositePrimaryKey('CRC_DATE', 'CRC_DESC', 'CRC_BAL')
    crc_date = models.DateField(db_column='CRC_DATE',  primary_key=True)  # Field name made lowercase.
    crc_num = models.CharField(db_column='CRC_NUM', max_length=15, blank=True, null=True)  # Field name made lowercase.
    crc_desc = models.CharField(db_column='CRC_DESC', max_length=100)  # Field name made lowercase.
    crc_deposit = models.DecimalField(db_column='CRC_DEPOSIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    crc_with = models.DecimalField(db_column='CRC_WITH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    crc_bal = models.DecimalField(db_column='CRC_BAL', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-crc_date']
        managed = False
        db_table = 'CHASE_RENT_CHK'
        unique_together = (('crc_date', 'crc_desc', 'crc_bal'),)


class ChaseVisaDtl(models.Model):
    #pk = models.CompositePrimaryKey('CVD_DATE', 'CVD_DEPOSIT', 'CVD_WITH')
    cvd_date = models.DateField(db_column='CVD_DATE',  primary_key=True)  # Field name made lowercase.
    cvd_desc = models.CharField(db_column='CVD_DESC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cvd_deposit = models.DecimalField(db_column='CVD_DEPOSIT', max_digits=10, decimal_places=2)  # Field name made lowercase.
    cvd_with = models.DecimalField(db_column='CVD_WITH', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-cvd_date']
        managed = False
        db_table = 'CHASE_VISA_DTL'
        unique_together = (('cvd_date', 'cvd_deposit', 'cvd_with'),)


class CommbankChkDtl(models.Model):
    cbd_date = models.DateField(db_column='CBD_DATE', blank=True, primary_key=True)  # Field name made lowercase.
    cbd_desc = models.CharField(db_column='CBD_DESC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cbd_deposit = models.DecimalField(db_column='CBD_DEPOSIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbd_with = models.DecimalField(db_column='CBD_WITH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbd_bal = models.DecimalField(db_column='CBD_BAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ordering = ['-cbd_date']
        managed = False
        db_table = 'COMMBANK_CHK_DTL'


class CommbankSvrDtl(models.Model):
    #pk = models.CompositePrimaryKey('CBD_DATE', 'CBD_DESC', 'CBD_BAL')
    cbd_date = models.DateField(db_column='CBD_DATE',  primary_key=True)  # Field name made lowercase.
    cbd_desc = models.CharField(db_column='CBD_DESC', max_length=100)  # Field name made lowercase.
    cbd_deposit = models.DecimalField(db_column='CBD_DEPOSIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbd_with = models.DecimalField(db_column='CBD_WITH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cbd_bal = models.DecimalField(db_column='CBD_BAL', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-cbd_date']
        managed = False
        db_table = 'COMMBANK_SVR_DTL'
        unique_together = (('cbd_date', 'cbd_desc', 'cbd_bal'), ('cbd_date', 'cbd_desc', 'cbd_bal'),)


class FiaAmexDtl(models.Model):
    fiaam_date = models.DateField(db_column='FIAAM_DATE', blank=True, primary_key=True)  # Field name made lowercase.
    fiaam_desc = models.CharField(db_column='FIAAM_DESC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fiaam_deposit = models.DecimalField(db_column='FIAAM_DEPOSIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fiaam_with = models.DecimalField(db_column='FIAAM_WITH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ordering = ['-fiaam_date']
        managed = False
        db_table = 'FIA_AMEX_DTL'


class FidelityBankDtl(models.Model):
    #pk = models.CompositePrimaryKey('FBD_DATE', 'FBD_DESC', 'FBD_BAL')
    fbd_date = models.DateField(db_column='FBD_DATE',  primary_key=True)  # Field name made lowercase.
    fbd_num = models.CharField(db_column='FBD_NUM', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fbd_desc = models.CharField(db_column='FBD_DESC', max_length=100)  # Field name made lowercase.
    fbd_deposit = models.DecimalField(db_column='FBD_DEPOSIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fbd_with = models.DecimalField(db_column='FBD_WITH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fbd_bal = models.DecimalField(db_column='FBD_BAL', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-fbd_date']
        managed = False
        db_table = 'FIDELITY_BANK_DTL'
        unique_together = (('fbd_date', 'fbd_desc', 'fbd_bal'), ('fbd_date', 'fbd_desc', 'fbd_bal'),)


class FidelityMfTbl(models.Model):
    fmt_trade_dt = models.DateField(db_column='FMT_TRADE_DT', blank=True, primary_key=True)  # Field name made lowercase.
    fmt_mf = models.CharField(db_column='FMT_MF', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fmt_qty = models.DecimalField(db_column='FMT_QTY', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fmt_price = models.DecimalField(db_column='FMT_PRICE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fmt_tran = models.CharField(db_column='FMT_TRAN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    fmt_value = models.DecimalField(db_column='FMT_VALUE', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fmt_bal = models.DecimalField(db_column='FMT_BAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ordering = ['-fmt_trade_dt']
        managed = False
        db_table = 'FIDELITY_MF_TBL'


class FifthrdBankDtl(models.Model):
    #pk = models.CompositePrimaryKey('FTBD_DATE', 'FTBD_DESC', 'FTBD_BAL')
    ftbd_date = models.DateField(db_column='FTBD_DATE',  primary_key=True)  # Field name made lowercase.
    ftbd_num = models.CharField(db_column='FTBD_NUM', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ftbd_desc = models.CharField(db_column='FTBD_DESC', max_length=100)  # Field name made lowercase.
    ftbd_deposit = models.DecimalField(db_column='FTBD_DEPOSIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ftbd_with = models.DecimalField(db_column='FTBD_WITH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ftbd_bal = models.DecimalField(db_column='FTBD_BAL', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-ftbd_date']
        managed = False
        db_table = 'FIFTHRD_BANK_DTL'
        unique_together = (('ftbd_date', 'ftbd_desc', 'ftbd_bal'), ('ftbd_date', 'ftbd_desc', 'ftbd_bal'),)


class HdfcBankDtl(models.Model):
    #pk = models.CompositePrimaryKey('HBD_DATE', 'HBD_DESC', 'HBD_BAL')
    hbd_date = models.DateField(db_column='HBD_DATE',  primary_key=True)  # Field name made lowercase.
    hbd_num = models.CharField(db_column='HBD_NUM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    hbd_desc = models.CharField(db_column='HBD_DESC', max_length=100)  # Field name made lowercase.
    hbd_deposit = models.DecimalField(db_column='HBD_DEPOSIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    hbd_with = models.DecimalField(db_column='HBD_WITH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    hbd_bal = models.DecimalField(db_column='HBD_BAL', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-hbd_date']
        managed = False
        db_table = 'HDFC_BANK_DTL'
        unique_together = (('hbd_date', 'hbd_desc', 'hbd_bal'), ('hbd_date', 'hbd_desc', 'hbd_bal'),)


class IciciBankDtl(models.Model):
    #pk = models.CompositePrimaryKey('IBD_DATE', 'IBD_DESC', 'IBD_BAL')
    ibd_date = models.DateField(db_column='IBD_DATE',  primary_key=True)  # Field name made lowercase.
    ibd_num = models.CharField(db_column='IBD_NUM', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ibd_desc = models.CharField(db_column='IBD_DESC', max_length=100)  # Field name made lowercase.
    ibd_deposit = models.DecimalField(db_column='IBD_DEPOSIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ibd_with = models.DecimalField(db_column='IBD_WITH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ibd_bal = models.DecimalField(db_column='IBD_BAL', max_digits=10, decimal_places=2)  # Field name made lowercase.
    ibd_auto_sweep = models.DecimalField(db_column='IBD_AUTO_SWEEP', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    ibd_rev_sweep = models.DecimalField(db_column='IBD_REV_SWEEP', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ordering = ['-ibd_date']
        managed = False
        db_table = 'ICICI_BANK_DTL'
        unique_together = (('ibd_date', 'ibd_desc', 'ibd_bal'), ('ibd_date', 'ibd_desc', 'ibd_bal'),)


class MutualFundInv(models.Model):
    #pk = models.CompositePrimaryKey('MFI_MF_NAME', 'MFI_TRAN_DATE', 'MFI_TRAN', 'MFI_AMT')
    mfi_mf_name = models.CharField(db_column='MFI_MF_NAME', max_length=100)  # Field name made lowercase.
    mfi_tran_date = models.DateField(db_column='MFI_TRAN_DATE',  primary_key=True)  # Field name made lowercase.
    mfi_tran = models.CharField(db_column='MFI_TRAN', max_length=10)  # Field name made lowercase.
    mfi_amt = models.DecimalField(db_column='MFI_AMT', max_digits=10, decimal_places=2)  # Field name made lowercase.
    mfi_pub_nav = models.DecimalField(db_column='MFI_PUB_NAV', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mfi_tran_nav = models.DecimalField(db_column='MFI_TRAN_NAV', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mfi_tran_qty = models.DecimalField(db_column='MFI_TRAN_QTY', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    mfi_bal_qty = models.DecimalField(db_column='MFI_BAL_QTY', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ordering = ['-mfi_tran_date']
        managed = False
        db_table = 'MUTUAL_FUND_INV'
        unique_together = (('mfi_mf_name', 'mfi_tran_date', 'mfi_tran', 'mfi_amt'), ('mfi_mf_name', 'mfi_tran_date', 'mfi_tran', 'mfi_amt'),)


class RothWf401(models.Model):
    rwf_tran_date = models.DateField(db_column='RWF_TRAN_DATE', blank=True, primary_key=True)  # Field name made lowercase.
    rwf_invmt = models.CharField(db_column='RWF_INVMT', max_length=40, blank=True, null=True)  # Field name made lowercase.
    rwf_tran = models.CharField(db_column='RWF_TRAN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    rwf_tran_amt = models.DecimalField(db_column='RWF_TRAN_AMT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rwf_tran_unit = models.DecimalField(db_column='RWF_TRAN_UNIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    rwf_unit_val = models.DecimalField(db_column='RWF_UNIT_VAL', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ordering = ['-rwf_tran_date']
        managed = False
        db_table = 'ROTH_WF_401'


class SuntrustBankDtl(models.Model):
    #pk = models.CompositePrimaryKey('SBD_DATE', 'SBD_DESC', 'SBD_BAL')
    sbd_date = models.DateField(db_column='SBD_DATE',  primary_key=True)  # Field name made lowercase.
    sbd_num = models.CharField(db_column='SBD_NUM', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sbd_desc = models.CharField(db_column='SBD_DESC', max_length=100)  # Field name made lowercase.
    sbd_deposit = models.DecimalField(db_column='SBD_DEPOSIT', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sbd_with = models.DecimalField(db_column='SBD_WITH', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    sbd_bal = models.DecimalField(db_column='SBD_BAL', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-sbd_date']
        managed = False
        db_table = 'SUNTRUST_BANK_DTL'
        unique_together = (('sbd_date', 'sbd_desc', 'sbd_bal'),)


class UsaStockTbl(models.Model):
    #pk = models.CompositePrimaryKey('UST_TICK', 'UST_PRICE', 'UST_TRAN', 'UST_DATE', 'UST_QTY')
    ust_tick = models.CharField(db_column='UST_TICK', max_length=6)  # Field name made lowercase.
    ust_name = models.CharField(db_column='UST_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ust_tran = models.CharField(db_column='UST_TRAN', max_length=4)  # Field name made lowercase.
    ust_date = models.DateField(db_column='UST_DATE',  primary_key=True)  # Field name made lowercase.
    ust_qty = models.DecimalField(db_column='UST_QTY', max_digits=10, decimal_places=2)  # Field name made lowercase.
    ust_price = models.DecimalField(db_column='UST_PRICE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    ust_commision = models.DecimalField(db_column='UST_COMMISION', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        ordering = ['-ust_date']
        managed = False
        db_table = 'USA_STOCK_TBL'
        unique_together = (('ust_tick', 'ust_price', 'ust_tran', 'ust_date', 'ust_qty'),)



class WellsFargoVisaDtl(models.Model):
    #pk = models.CompositePrimaryKey('WFVD_DATE', 'WFVD_DESC', 'WFVD_DEPOSIT', 'WFVD_WITH')
    wfvd_date = models.DateField(db_column='WFVD_DATE',  primary_key=True)  # Field name made lowercase.
    wfvd_desc = models.CharField(db_column='WFVD_DESC', max_length=100)  # Field name made lowercase.
    wfvd_deposit = models.DecimalField(db_column='WFVD_DEPOSIT', max_digits=10, decimal_places=2)  # Field name made lowercase.
    wfvd_with = models.DecimalField(db_column='WFVD_WITH', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        ordering = ['-wfvd_date']
        managed = False
        db_table = 'WELLS_FARGO_VISA_DTL'
        unique_together = (('wfvd_date', 'wfvd_desc', 'wfvd_deposit', 'wfvd_with'), ('wfvd_date', 'wfvd_desc', 'wfvd_deposit', 'wfvd_with'),)
