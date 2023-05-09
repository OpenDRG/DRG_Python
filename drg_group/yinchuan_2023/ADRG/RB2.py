from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCR_DRG

def group(record):
  adrg_zd=["C81.000","C81.100","C81.200","C81.700","C83.300","C84.600","C84.700","C85.100x021","C85.900","C86.000","C90.000","C90.000x027","C90.000x028","C90.000x040"]
  adrg_zd1=[]
  adrg_ss=["99.2503","99.2504"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合RB2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCR_DRG.RB21_group(record):
      return 'RB21'

    if MDCR_DRG.RB25_group(record):
      return 'RB25'

    return 'RB2'
  else:
    return ''

