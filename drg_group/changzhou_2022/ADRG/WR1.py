from drg_group.changzhou_2022.Base import message,intersect,SS_VALID
from drg_group.changzhou_2022.DRG import MDCW_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True:
    message('符合WR1入组条件，匹配规则：')
    
    if MDCW_DRG.WR13_group(record):
      return 'WR13'

    if MDCW_DRG.WR15_group(record):
      return 'WR15'

    return 'WR1'
  else:
    return ''

