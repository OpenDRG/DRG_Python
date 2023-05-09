from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCR_DRG

def group(record):
  adrg_zd=["C91.000","C91.000x009","C91.000x013","C91.000x016","C91.001","C92.000","C92.000x003","C92.000x014","C92.000x016","C92.000x017","C92.000x018","C92.002","C92.003","C92.004","C92.401","C92.402","C92.501","C93.003","C93.100x012","C95.000","C95.000x018","C95.000x117"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合RR1入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RR11_group(record):
      return 'RR11'

    if MDCR_DRG.RR13_group(record):
      return 'RR13'

    if MDCR_DRG.RR15_group(record):
      return 'RR15'

    return 'RR1'
  else:
    return ''

