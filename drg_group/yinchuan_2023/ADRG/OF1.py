from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCO_DRG

def group(record):
  adrg_zd=["O01.101","O02.000x001","O04.901","O04.902","O35.004","O35.101","O35.102","O35.800x003","O35.800x011","O35.800x012","O35.801","O35.804","O35.814","O35.819","O35.823"]
  adrg_zd1=[]
  adrg_ss=["69.0200x003","73.1x01","75.0x01","75.0x02"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合OF1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCO_DRG.OF19_group(record):
      return 'OF19'

    return 'OF1'
  else:
    return ''

