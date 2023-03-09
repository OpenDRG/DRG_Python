from drg_group.lanzhou_2022.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2022.DRG import MDCS_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in SS_VALID:
    message('符合SB1入组条件，匹配规则：存在手术')
    
    if MDCS_DRG.SB11_group(record):
      return 'SB11'

    if MDCS_DRG.SB1B_group(record):
      return 'SB14'

    return 'SB1'
  else:
    return ''

