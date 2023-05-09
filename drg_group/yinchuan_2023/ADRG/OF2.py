from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCO_DRG

def group(record):
  adrg_zd=["O02.100","O03.001","O03.101","O03.400x001","O03.901","O04.001","O04.100x002","O04.300","O04.400","O04.401","O04.402","O04.800","O04.900x001","O04.905","O07.402","O08.004"]
  adrg_zd1=[]
  adrg_ss=["69.0100x002","69.0101","69.0201","69.5101","69.5102","69.5103","69.5202","69.5901","73.4x00x004","96.4902"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合OF2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCO_DRG.OF29_group(record):
      return 'OF29'

    return 'OF2'
  else:
    return ''

