from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCT_DRG

def group(record):
  adrg_zd=["F32.000x011","F32.200","F32.900","F32.901","F39.x00"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合TS1入组条件，匹配规则：主诊断匹配')
    
    if MDCT_DRG.TS19_group(record):
      return 'TS19'

    return 'TS1'
  else:
    return ''

