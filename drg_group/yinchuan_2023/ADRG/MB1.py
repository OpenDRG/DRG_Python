from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCM_DRG

def group(record):
  adrg_zd=["C61.x00","D29.100","D40.001","N40.x00","N41.200","N42.102"]
  adrg_zd1=[]
  adrg_ss=["60.0x00x003","60.0x02","60.2100x001","60.2100x002","60.2900x003","60.2900x004","60.2901","60.2902","60.6100x001","60.6100x002","60.6900x001","60.9401"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合MB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCM_DRG.MB19_group(record):
      return 'MB19'

    return 'MB1'
  else:
    return ''

