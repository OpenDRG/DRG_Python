from drg_group.lanzhou_2023.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["39.9500","39.9500x004","39.9500x005","39.9500x006","39.9500x007","39.9501","39.9600x002","39.9600x003","54.9800","54.9800x005","54.9800x006","54.9800x007","54.9800x008"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合LL1入组条件，匹配规则：主手术匹配')
    
    if MDCL_DRG.LL11_group(record):
      return 'LL11'

    if MDCL_DRG.LL1B_group(record):
      return 'LL14'

    return 'LL1'
  else:
    return ''

