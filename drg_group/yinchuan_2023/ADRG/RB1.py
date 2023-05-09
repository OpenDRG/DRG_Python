from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCR_DRG

def group(record):
  adrg_zd=["C91.000","C91.000x009","C91.002","C92.000","C92.002","C92.400x011","C93.003"]
  adrg_zd1=[]
  adrg_ss=["99.2503"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合RB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCR_DRG.RB11_group(record):
      return 'RB11'

    if MDCR_DRG.RB13_group(record):
      return 'RB13'

    return 'RB1'
  else:
    return ''

