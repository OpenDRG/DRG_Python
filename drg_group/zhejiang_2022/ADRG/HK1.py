from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCH_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["39.5017","42.3307","42.3308","42.3309","42.3310","42.9100x002","43.4100x020"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合HK1入组条件，匹配规则：某一手术匹配')
    
    if MDCH_DRG.HK11_group(record):
      return 'HK11'

    if MDCH_DRG.HK13_group(record):
      return 'HK13'

    return 'HK1'
  else:
    return ''

