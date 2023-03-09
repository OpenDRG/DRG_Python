from drg_group.lanzhou_2022.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2022.DRG import MDCV_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["21.9900x002","21.9900x005","21.9901","21.9902","79.6100","79.6201","79.6202","79.6301","79.6302","79.6400","79.6500","79.6601","79.6602","79.6701","79.6702","79.6800","79.6900x002","79.6901","83.4500x001","83.4501","83.4502","86.2200x011","86.2201","86.2202","86.2800x012"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合VC1入组条件，匹配规则：主手术匹配')
    
    if MDCV_DRG.VC11_group(record):
      return 'VC11'

    if MDCV_DRG.VC13_group(record):
      return 'VC13'

    if MDCV_DRG.VC15_group(record):
      return 'VC15'

    return 'VC1'
  else:
    return ''

