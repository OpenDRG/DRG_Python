from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCM_DRG

def group(record):
  adrg_zd=["C60.100","C60.201","C60.900","C61.x00","C62.900","C63.200","C63.201","D07.500","D40.001","D40.101","D40.901"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合MR1入组条件，匹配规则：主诊断匹配')
    
    if MDCM_DRG.MR11_group(record):
      return 'MR11'

    if MDCM_DRG.MR13_group(record):
      return 'MR13'

    if MDCM_DRG.MR15_group(record):
      return 'MR15'

    return 'MR1'
  else:
    return ''

