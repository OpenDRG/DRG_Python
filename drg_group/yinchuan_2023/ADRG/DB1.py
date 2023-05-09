from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCD_DRG

def group(record):
  adrg_zd=["D18.004","D36.703"]
  adrg_zd1=[]
  adrg_ss=["38.6201"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合DB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCD_DRG.DB19_group(record):
      return 'DB19'

    return 'DB1'
  else:
    return ''

