from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCR_DRG

def group(record):
  adrg_zd=["C90.000x021","C90.000x022","C90.000x033","C90.200"]
  adrg_zd1=[]
  adrg_ss=["45.6204","45.7300x007","54.4x06","54.5903"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合RA3入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCR_DRG.RA39_group(record):
      return 'RA39'

    return 'RA3'
  else:
    return ''

