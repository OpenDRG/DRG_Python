from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCH_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["51.2100","51.2200","51.2200x004","51.2201","51.2300","51.2301","51.2400"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合HC1入组条件，匹配规则：某一手术匹配')
    
    if MDCH_DRG.HC11_group(record):
      return 'HC11'

    if MDCH_DRG.HC13_group(record):
      return 'HC13'

    return 'HC1'
  else:
    return ''

