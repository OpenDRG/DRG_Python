from drg_group.yunnan_2023.Base import message,intersect,SS_VALID
from drg_group.yunnan_2023.DRG import MDCT_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and intersect(record.ssList,SS_VALID):
    message('符合TB1入组条件，匹配规则：存在手术')
    
    
    if MDCT_DRG.TB11_group(record):
      return 'TB11'

    if MDCT_DRG.TB15_group(record):
      return 'TB15'

    return ''
  else:
    return ''
