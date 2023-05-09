from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCM_DRG

def group(record):
  adrg_zd=["C60.900","D18.000x815","D18.000x855","D29.001","D29.700x005","I86.101","N47.x00x001","N47.x01","N47.x02","N47.x03","N48.600","N48.811","N48.901","Q53.202","Q54.000","Q54.100","Q54.900","Q55.202","Q55.603","Q55.604","Q55.606","Q55.801","Q55.802","S39.904"]
  adrg_zd1=[]
  adrg_ss=["38.5702","64.2x00x002","64.2x01","64.3x01","64.4300","64.4400","64.4901","64.4902","64.4903","64.4904","64.9100x002","64.9100x003","64.9101","64.9801"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合MC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCM_DRG.MC19_group(record):
      return 'MC19'

    return 'MC1'
  else:
    return ''

