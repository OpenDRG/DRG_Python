from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCX_DRG

def group(record):
  adrg_zd=["B90.902","R10.200x001","R10.201","R13.x00","R47.003","R47.100x001","R47.801","R47.802","R49.800x003","R53.x00x001","R53.x00x003","R62.000x003","R62.801","Z50.000"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合XR3入组条件，匹配规则：主诊断匹配')
    
    if MDCX_DRG.XR31_group(record):
      return 'XR31'

    if MDCX_DRG.XR33_group(record):
      return 'XR33'

    if MDCX_DRG.XR35_group(record):
      return 'XR35'

    return 'XR3'
  else:
    return ''

