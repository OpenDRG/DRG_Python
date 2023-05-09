from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I06.000","I35.000","I35.100","I35.200","I37.000","Q22.100"]
  adrg_zd1=[]
  adrg_ss=["35.0501","35.0502","35.9601"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FL3入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FL39_group(record):
      return 'FL39'

    return 'FL3'
  else:
    return ''

