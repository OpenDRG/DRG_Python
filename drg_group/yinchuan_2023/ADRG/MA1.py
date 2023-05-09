from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCM_DRG

def group(record):
  adrg_zd=["C60.100","C60.200","C60.900","C61.x00","C62.100","C62.900","D40.100x002","D40.101"]
  adrg_zd1=[]
  adrg_ss=["40.2400","40.5400x001","60.2100x001","60.5x02","60.6101","60.6900x002","62.2x01","62.3x00","62.3x01","62.4100x004","62.4101","64.3x01"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合MA1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCM_DRG.MA19_group(record):
      return 'MA19'

    return 'MA1'
  else:
    return ''

