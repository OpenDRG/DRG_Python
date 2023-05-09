from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCK_DRG

def group(record):
  adrg_zd=["D35.000","E11.500x043","E11.500x051","E11.503","E14.500x050","E27.801"]
  adrg_zd1=[]
  adrg_ss=["52.5901","54.4x02","54.5901","86.2200x011","86.2800x012","86.7400x026","86.7500x001","86.8900x011"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合KJ1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCK_DRG.KJ11_group(record):
      return 'KJ11'

    if MDCK_DRG.KJ15_group(record):
      return 'KJ15'

    return 'KJ1'
  else:
    return ''

