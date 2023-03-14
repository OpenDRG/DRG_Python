from drg_group.xian_2020.Base import message,intersect,SS_VALID
from drg_group.xian_2020.DRG import MDCY_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True:
    message('符合YC1入组条件，匹配规则：')
    
    if MDCY_DRG.YC11_group(record):
      return 'YC11'

    if MDCY_DRG.YC13_group(record):
      return 'YC13'

    if MDCY_DRG.YC15_group(record):
      return 'YC15'

    return 'YC1'
  else:
    return ''

