from drg_group.anyang_2021.Base import message,intersect,SS_VALID
from drg_group.anyang_2021.DRG import MDCT_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in SS_VALID:
    message('符合TB1入组条件，匹配规则：存在手术')
    
    if MDCT_DRG.TB19_group(record):
      return 'TB19'

    return ''
  else:
    return ''

