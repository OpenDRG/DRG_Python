from drg_group.changzhou_2022.Base import message,intersect,SS_VALID
from drg_group.changzhou_2022.DRG import MDCH_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["39.5017","42.3307","42.3308","42.3309","42.3310","43.4100x020","96.0601"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合HK1入组条件，匹配规则：主手术匹配')
    
    if MDCH_DRG.HK19_group(record):
      return 'HK19'

    return 'HK1'
  else:
    return ''

