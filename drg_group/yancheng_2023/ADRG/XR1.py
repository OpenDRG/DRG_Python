from drg_group.yancheng_2023.Base import message,intersect,SS_VALID
from drg_group.yancheng_2023.DRG import MDCX_DRG

def group(record):
  adrg_zd=["R41.000","R41.001","R41.300x001","R41.800x002","R46.600","R46.700","R53.x00x005","R63.200","R63.300x003","R63.601","T97.x01","Z00.401","Z04.601","Z50.100x001","Z50.200","Z50.300","Z50.400x001","Z50.500","Z50.700x001","Z50.800x002","Z50.900x001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合XR1入组条件，匹配规则：主诊断匹配')
    
    if MDCX_DRG.XR11_group(record):
      return 'XR11'

    if MDCX_DRG.XR13_group(record):
      return 'XR13'

    if MDCX_DRG.XR15_group(record):
      return 'XR15'

    return 'XR1'
  else:
    return ''

