from drg_group.qingdao_2023.Base import message,intersect,SS_VALID
from drg_group.qingdao_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["51.2100","51.2101","51.2200","51.2200x004","51.2201","51.2300","51.2301","51.2400","51.2401"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合HC2入组条件，匹配规则：主手术匹配')
    
    if MDCH_DRG.HC23_group(record):
      return 'HC23'

    if MDCH_DRG.HC25_group(record):
      return 'HC25'

    return 'HC2'
  else:
    return ''

