from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCU_DRG

def group(record):
  adrg_zd=["F10.201","F10.300","T51.001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合UR1入组条件，匹配规则：主诊断匹配')
    
    if MDCU_DRG.UR13_group(record):
      return 'UR13'

    if MDCU_DRG.UR15_group(record):
      return 'UR15'

    return 'UR1'
  else:
    return ''

