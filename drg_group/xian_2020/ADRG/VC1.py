from drg_group.xian_2020.Base import message,intersect,SS_VALID
from drg_group.xian_2020.DRG import MDCV_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["08.2000x009","08.2000x010","21.3200x010","21.3200x011","21.9900x002","27.4300x010","27.4300x011","54.3x00x011","61.3x00x005","61.3x00x006","64.2x00x006","64.2x00x007","71.3x00x021","71.3x00x022","71.3x00x023","71.3x00x024","85.2000x001","85.2000x002","86.2200x011","86.2201","86.2202","86.2800x012"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合VC1入组条件，匹配规则：主手术匹配')
    
    if MDCV_DRG.VC19_group(record):
      return 'VC19'

    return 'VC1'
  else:
    return ''

