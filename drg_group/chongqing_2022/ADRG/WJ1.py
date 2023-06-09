from drg_group.chongqing_2022.Base import message,intersect,SS_VALID
from drg_group.chongqing_2022.DRG import MDCW_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in SS_VALID:
    message('符合WJ1入组条件，匹配规则：存在手术')
    
    
    if MDCW_DRG.WJ11_group(record):
      return 'WJ11'

    if MDCW_DRG.WJ13_group(record):
      return 'WJ13'

    if MDCW_DRG.WJ15_group(record):
      return 'WJ15'

    return ''
  else:
    return ''
