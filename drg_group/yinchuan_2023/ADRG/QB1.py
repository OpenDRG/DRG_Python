from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCQ_DRG

def group(record):
  adrg_zd=["D13.901","D18.000x044","D18.100x023","D58.000","D73.100","D73.400","D73.500","D73.501","D73.805","R16.100x001","S36.002"]
  adrg_zd1=[]
  adrg_ss=["41.2x03","41.4200x002","41.4300","41.5x00","41.5x01","41.9400","41.9501"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合QB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCQ_DRG.QB13_group(record):
      return 'QB13'

    if MDCQ_DRG.QB15_group(record):
      return 'QB15'

    return 'QB1'
  else:
    return ''

