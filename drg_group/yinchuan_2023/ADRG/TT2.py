from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCT_DRG

def group(record):
  adrg_zd=["F52.400","R45.800x091","R46.200x002","R46.400","Z03.200"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合TT2入组条件，匹配规则：主诊断匹配')
    
    if MDCT_DRG.TT23_group(record):
      return 'TT23'

    if MDCT_DRG.TT25_group(record):
      return 'TT25'

    return 'TT2'
  else:
    return ''

