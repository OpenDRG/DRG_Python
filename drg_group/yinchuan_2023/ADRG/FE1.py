from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I77.202","Q25.701"]
  adrg_zd1=[]
  adrg_ss=["39.7900x517"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FE1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FE19_group(record):
      return 'FE19'

    return 'FE1'
  else:
    return ''

