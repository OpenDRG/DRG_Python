from drg_group.tongchuan_2022.Base import message,intersect,SS_VALID
from drg_group.tongchuan_2022.DRG import MDCY_DRG

def group(record):
  adrg_zd=["R75.x00x001","Z20.600","Z21.x00x001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合YR2入组条件，匹配规则：主诊断匹配')
    
    if MDCY_DRG.YR29_group(record):
      return 'YR29'

    return 'YR2'
  else:
    return ''

