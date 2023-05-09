from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCV_DRG

def group(record):
  adrg_zd=["N99.401","T81.000x001","T81.000x009","T81.000x010","T81.000x019","T81.000x021","T81.000x023","T81.000x039","T81.005","T81.012","T81.015","T81.018","T81.019","T81.021","T81.022","T81.024","T81.026","T81.208","T81.209","T81.301","T81.400x012","T81.400x013","T81.400x014","T81.407","T81.408","T81.412","T81.800x001","T81.800x017","T81.806","T81.807","T81.808","T81.809","T81.811","T81.812","T81.813","T85.500x001","T85.600","T85.600x004","T85.610","T85.700","T86.808","T88.101"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合VT1入组条件，匹配规则：主诊断匹配')
    
    if MDCV_DRG.VT13_group(record):
      return 'VT13'

    if MDCV_DRG.VT15_group(record):
      return 'VT15'

    return 'VT1'
  else:
    return ''

