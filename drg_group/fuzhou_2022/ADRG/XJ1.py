from drg_group.fuzhou_2022.Base import message,intersect,SS_VALID
from drg_group.fuzhou_2022.DRG import MDCX_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in SS_VALID:
    message('符合XJ1入组条件，匹配规则：存在手术')
    
    if MDCX_DRG.XJ13_group(record):
      return 'XJ13'

    if MDCX_DRG.XJ15_group(record):
      return 'XJ15'

    return 'XJ1'
  else:
    return ''

