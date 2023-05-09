from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCV_DRG

def group(record):
  adrg_zd=["T67.000x001","T67.001","T67.200","T67.500","T67.500x001","T67.901","T68.x00","T70.202","T71.x00","T71.x00x003","T75.100x001","T75.300","T75.400x001","T79.400","T79.501","T79.800x003"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合VZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCV_DRG.VZ11_group(record):
      return 'VZ11'

    if MDCV_DRG.VZ13_group(record):
      return 'VZ13'

    if MDCV_DRG.VZ15_group(record):
      return 'VZ15'

    return 'VZ1'
  else:
    return ''

