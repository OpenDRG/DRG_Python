from drg_group.wuhan_2022.Base import message,intersect,SS_VALID
from drg_group.wuhan_2022.DRG import MDCY_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True:
    message('符合YR1入组条件，匹配规则：')
    
    if MDCY_DRG.YR11_group(record):
      return 'YR11'

    if MDCY_DRG.YR13_group(record):
      return 'YR13'

    if MDCY_DRG.YR15_group(record):
      return 'YR15'

    return 'YR1'
  else:
    return ''

