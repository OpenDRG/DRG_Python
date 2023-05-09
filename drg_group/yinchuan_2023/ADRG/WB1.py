from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCW_DRG

def group(record):
  adrg_zd=["T23.300x003","T24.300x003","T24.300x004"]
  adrg_zd1=[]
  adrg_ss=["86.6200x002","86.6201","86.6901","86.6906"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合WB1入组条件，匹配规则：主诊断匹配、某一手术匹配')
    
    if MDCW_DRG.WB19_group(record):
      return 'WB19'

    return 'WB1'
  else:
    return ''

