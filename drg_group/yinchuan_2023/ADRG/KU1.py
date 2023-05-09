from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCK_DRG

def group(record):
  adrg_zd=["E41.x01","E43.x00","E43.x00x001","E43.x00x002","E44.000","E44.100","E45.x00x003","E46.x00x002","E46.x00x003","E53.802","E53.804","E55.002","E55.900","E56.100","R64.x00"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合KU1入组条件，匹配规则：主诊断匹配')
    
    if MDCK_DRG.KU11_group(record):
      return 'KU11'

    if MDCK_DRG.KU13_group(record):
      return 'KU13'

    if MDCK_DRG.KU15_group(record):
      return 'KU15'

    return 'KU1'
  else:
    return ''

