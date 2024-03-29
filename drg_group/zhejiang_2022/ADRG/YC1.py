from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCY_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in SS_VALID:
    message('符合YC1入组条件，匹配规则：存在手术')
    
    if MDCY_DRG.YC19_group(record):
      return 'YC19'

    return ''
  else:
    return ''

