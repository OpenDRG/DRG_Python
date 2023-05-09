from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCK_DRG

def group(record):
  adrg_zd=["D35.200","D35.200x008","D35.200x009","D35.200x010","E23.608"]
  adrg_zd1=[]
  adrg_ss=["07.6200x003","07.6200x007","07.6201","07.6202","07.6301"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合KC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCK_DRG.KC19_group(record):
      return 'KC19'

    return 'KC1'
  else:
    return ''

