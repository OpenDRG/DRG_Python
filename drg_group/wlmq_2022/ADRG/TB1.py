from drg_group.wlmq_2022.Base import message,intersect,SS_VALID
from drg_group.wlmq_2022.DRG import MDCT_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in SS_VALID:
    message('符合TB1入组条件，匹配规则：存在手术')
    
    if MDCT_DRG.TB13_group(record):
      return 'TB13'

    if MDCT_DRG.TB15_group(record):
      return 'TB15'

    return 'TB1'
  else:
    return ''

