from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["A16.500x010","J85.300","J86.012","J98.600x001","S27.811"]
  adrg_zd1=[]
  adrg_ss=["34.1x01","34.1x05","34.5200x001","34.7302","34.8200x002"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合EC2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCE_DRG.EC29_group(record):
      return 'EC29'

    return 'EC2'
  else:
    return ''

