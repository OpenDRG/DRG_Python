from drg_group.wuhan_2022.Base import message,intersect,SS_VALID
from drg_group.wuhan_2022.DRG import MDCY_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True:
    message('符合YR2入组条件，匹配规则：')
    
    if MDCY_DRG.YR29_group(record):
      return 'YR29'

    return 'YR2'
  else:
    return ''

