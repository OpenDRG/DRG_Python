from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCR_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.1000","00.1500x002","99.2500x017","99.2500x036","99.2500x037","99.2502","99.2503","99.2505","99.2506","99.2800x003","99.2800x006","99.2801"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合RB1入组条件，匹配规则：某一手术匹配')
    
    if MDCR_DRG.RB11_group(record):
      return 'RB11'

    if MDCR_DRG.RB13_group(record):
      return 'RB13'

    if MDCR_DRG.RB15_group(record):
      return 'RB15'

    return 'RB1'
  else:
    return ''

