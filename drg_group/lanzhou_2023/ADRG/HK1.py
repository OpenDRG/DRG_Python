from drg_group.lanzhou_2023.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["43.4100x020","96.0601"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合HK1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCH_DRG.HK11_group(record):
      return 'HK11'

    if MDCH_DRG.HK1B_group(record):
      return 'HK14'

    return 'HK1'
  else:
    return ''

