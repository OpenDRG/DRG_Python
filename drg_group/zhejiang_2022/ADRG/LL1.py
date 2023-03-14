from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCL_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["39.9500x005","39.9500x006","39.9500x007","39.9501","39.9600x002","39.9600x003","39.9700x001","39.9701","39.9702","39.9703","39.9704","39.9705","54.9800","54.9800x005","54.9800x006","54.9800x007","54.9800x008"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合LL1入组条件，匹配规则：某一手术匹配')
    
    if MDCL_DRG.LL11_group(record):
      return 'LL11'

    if MDCL_DRG.LL13_group(record):
      return 'LL13'

    if MDCL_DRG.LL15_group(record):
      return 'LL15'

    return 'LL1'
  else:
    return ''

