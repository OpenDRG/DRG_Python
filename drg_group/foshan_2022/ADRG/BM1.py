from drg_group.foshan_2022.Base import message,intersect,SS_VALID
from drg_group.foshan_2022.DRG import MDCB_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["88.4100x001","88.4101","88.4102","88.4103","88.4104","88.4401","88.6101","88.6102","88.6103"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合BM1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    
    if MDCB_DRG.BM11_group(record):
      return 'BM11'

    if MDCB_DRG.BM13_group(record):
      return 'BM13'

    if MDCB_DRG.BM15_group(record):
      return 'BM15'

    return ''
  else:
    return ''

