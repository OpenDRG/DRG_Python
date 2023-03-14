from drg_group.xian_2020.Base import message,intersect,SS_VALID
from drg_group.xian_2020.DRG import MDCW_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True:
    message('符合WB1入组条件，匹配规则：')
    
    if MDCW_DRG.WB11_group(record):
      return 'WB11'

    if MDCW_DRG.WB13_group(record):
      return 'WB13'

    if MDCW_DRG.WB15_group(record):
      return 'WB15'

    return 'WB1'
  else:
    return ''

