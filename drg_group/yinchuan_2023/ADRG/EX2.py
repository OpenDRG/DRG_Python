from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["A37.900","A37.901+J17.0*","J20.000","J20.100","J20.200","J20.800","J20.900","J20.901","J20.902","J21.801","J21.900","J21.900x002","J21.901","J40.x00","J40.x01"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合EX2入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.EX23_group(record):
      return 'EX23'

    if MDCE_DRG.EX25_group(record):
      return 'EX25'

    return 'EX2'
  else:
    return ''

