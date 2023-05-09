from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["I63.402","I63.501","I63.900","I63.901","I63.902","I63.904","I63.905","I63.906","I63.907"]
  adrg_zd1=[]
  adrg_ss=["99.1005","99.1008","99.1009"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合BL1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCB_DRG.BL19_group(record):
      return 'BL19'

    return 'BL1'
  else:
    return ''

