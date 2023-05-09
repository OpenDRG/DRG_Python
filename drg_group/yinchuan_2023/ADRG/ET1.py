from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["D86.000","D86.200","J62.800x005","J62.803","J64.x00","J67.200x002","J67.900","J68.002","J70.001","J82.x01","J84.001","J84.100x007","J84.100x008","J84.101","J84.104","J84.108","J84.109","J84.800x004","J84.800x005","J84.800x006","J84.800x007","J84.803","J84.804","J84.900","M05.100+J99.0*","M05.101+J99.0*","M05.102+J99.0*","M32.103+J99.1*","M33.103+J99.1*","M33.201+J99.1*","M33.901+J99.1*","M34.800x001+J99.1*","M34.801+J99.1*","M35.002+J99.1*","M35.904+J99.1*","R04.800x004"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合ET1入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.ET11_group(record):
      return 'ET11'

    if MDCE_DRG.ET13_group(record):
      return 'ET13'

    if MDCE_DRG.ET15_group(record):
      return 'ET15'

    return 'ET1'
  else:
    return ''

