from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCX_DRG

def group(record):
  adrg_zd=["Q96.900","Q99.101","Q99.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合XT2入组条件，匹配规则：主诊断匹配')
    
    if MDCX_DRG.XT29_group(record):
      return 'XT29'

    return 'XT2'
  else:
    return ''

