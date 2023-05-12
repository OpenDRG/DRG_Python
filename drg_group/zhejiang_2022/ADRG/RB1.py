from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCR_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合RB1入组条件，匹配规则：主手术匹配')
    
    if MDCR_DRG.RB11_group(record):
      return 'RB11'

    if MDCR_DRG.RB13_group(record):
      return 'RB13'

    if MDCR_DRG.RB15_group(record):
      return 'RB15'

    return ''
  else:
    return ''

