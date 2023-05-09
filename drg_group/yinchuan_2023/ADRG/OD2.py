from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCO_DRG

def group(record):
  adrg_zd=["O03.901","O04.300","O04.401","O08.802","O08.803","O20.000","O23.500x009","O34.301","O34.400x011","O34.404","O34.406","O72.003","O73.002"]
  adrg_zd1=[]
  adrg_ss=["67.0x00","67.0x00x002","67.3203","67.3902","67.3904","67.5900x002","67.5900x003","67.5901","71.2200x002"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合OD2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCO_DRG.OD29_group(record):
      return 'OD29'

    return 'OD2'
  else:
    return ''

