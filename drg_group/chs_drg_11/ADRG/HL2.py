from drg_group.chs_drg_11.Base import message,intersect,SS_VALID
from drg_group.chs_drg_11.DRG import MDCH_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["51.1000","51.1100","51.1101","51.1104","51.1105","51.1500","52.1302","52.1303"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合HL2入组条件，匹配规则：主手术匹配')
    
    if MDCH_DRG.HL29_group(record):
      return 'HL29'

    return 'HL2'
  else:
    return ''

