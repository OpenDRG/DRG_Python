from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["S27.000","S27.100","S27.110","S27.200","S27.301","S27.801","S27.802","S27.808","S27.811","S29.700","S29.900","T79.800x007"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合EU1入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.EU19_group(record):
      return 'EU19'

    return 'EU1'
  else:
    return ''

