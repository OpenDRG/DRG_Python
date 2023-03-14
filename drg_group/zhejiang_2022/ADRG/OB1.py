from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCO_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["74.0x00","74.1x01","74.1x02","74.2x00","74.4x01","74.9900"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合OB1入组条件，匹配规则：某一手术匹配')
    
    if MDCO_DRG.OB11_group(record):
      return 'OB11'

    if MDCO_DRG.OB13_group(record):
      return 'OB13'

    if MDCO_DRG.OB15_group(record):
      return 'OB15'

    return 'OB1'
  else:
    return ''

