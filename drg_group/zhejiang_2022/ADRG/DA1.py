from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCD_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合DA1入组条件，匹配规则：主手术匹配')
    
    if MDCD_DRG.DA11_group(record):
      return 'DA11'

    if MDCD_DRG.DA13_group(record):
      return 'DA13'

    if MDCD_DRG.DA15_group(record):
      return 'DA15'

    return ''
  else:
    return ''

