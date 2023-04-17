from drg_group.lanzhou_2023.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2023.DRG import MDCW_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in SS_VALID:
    message('符合WJ1入组条件，匹配规则：存在手术')
    
    if MDCW_DRG.WJ1B_group(record):
      return 'WJ14'

    if MDCW_DRG.WJ11_group(record):
      return 'WJ11'

    return 'WJ1'
  else:
    return ''

