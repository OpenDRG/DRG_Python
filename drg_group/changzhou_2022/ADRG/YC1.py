from drg_group.changzhou_2022.Base import message,intersect,SS_VALID
from drg_group.changzhou_2022.DRG import MDCY_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True:
    message('符合YC1入组条件，匹配规则：')
    
    if MDCY_DRG.YC19_group(record):
      return 'YC19'

    return 'YC1'
  else:
    return ''

