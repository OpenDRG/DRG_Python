from drg_group.guangxi_2022.Base import message,intersect,SS_VALID
from drg_group.guangxi_2022.DRG import MDCH_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["51.1000","51.1100","51.1101","51.1104","51.1105","51.1500","52.1302","52.1303"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合HL2入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCH_DRG.HL21_group(record):
      return 'HL21'

    if MDCH_DRG.HL23_group(record):
      return 'HL23'

    if MDCH_DRG.HL25_group(record):
      return 'HL25'

    return 'HL2'
  else:
    return ''

