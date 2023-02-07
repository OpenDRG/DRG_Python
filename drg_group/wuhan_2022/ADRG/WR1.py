from drg_group.wuhan_2022.Base import message,intersect,SS_VALID
from drg_group.wuhan_2022.DRG import MDCW_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True:
    message('符合WR1入组条件，匹配规则：')
    
    if MDCW_DRG.WR11_group(record):
      return 'WR11'

    if MDCW_DRG.WR1B_group(record):
      return 'WR1B'

    return 'WR1'
  else:
    return ''

