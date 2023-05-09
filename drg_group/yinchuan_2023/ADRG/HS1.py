from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=["K70.401","K71.102","K72.000x004","K72.001","K72.003","K72.100"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合HS1入组条件，匹配规则：主诊断匹配')
    
    if MDCH_DRG.HS11_group(record):
      return 'HS11'

    if MDCH_DRG.HS15_group(record):
      return 'HS15'

    return 'HS1'
  else:
    return ''

