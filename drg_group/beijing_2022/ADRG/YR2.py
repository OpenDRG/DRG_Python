from drg_group.beijing_2022.Base import message,intersect,SS_VALID
from drg_group.beijing_2022.DRG import MDCY_DRG

def group(record):
  adrg_zd=["R75.x00x001","Z21.x00x001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and intersect(record.zdList,adrg_zd):
    message('符合YR2入组条件，匹配规则：某一诊断匹配')
    
    if MDCY_DRG.YR29_group(record):
      return 'YR29'

    return 'YR2'
  else:
    return ''

