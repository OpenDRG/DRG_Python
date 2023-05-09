from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["B37.100","B37.101+J17.2*","B44.000x001+J99.8*","B44.101+J99.8*","B44.102+J17.2*","B45.000","B48.501+J17.2*","B49.x14+J99.8*"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合ES2入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.ES21_group(record):
      return 'ES21'

    if MDCE_DRG.ES23_group(record):
      return 'ES23'

    if MDCE_DRG.ES25_group(record):
      return 'ES25'

    return 'ES2'
  else:
    return ''

