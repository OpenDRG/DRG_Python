from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=["C22.100","C24.000x007","C24.002","C25.000","C78.700","D13.500x001","K80.000x004","K80.001","K80.100x001","K80.101","K80.505","K80.506","K80.801","K82.200","K83.001","K83.104","K83.107","K83.109","K83.502","K85.101","K91.807","Q44.400","Q44.504"]
  adrg_zd1=[]
  adrg_ss=["51.0300x002","51.0301","51.0400x004","51.0400x008","51.0401","51.0405","51.3203","51.3901","51.3907","51.5900x001","51.5901","51.6900x007","51.6900x012","51.6900x013","51.6901","51.6902","51.6905","51.7900x002","51.7901","51.7906"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合HC3入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCH_DRG.HC31_group(record):
      return 'HC31'

    if MDCH_DRG.HC33_group(record):
      return 'HC33'

    if MDCH_DRG.HC35_group(record):
      return 'HC35'

    return 'HC3'
  else:
    return ''

