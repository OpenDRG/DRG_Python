from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCN_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["65.9900x006","69.9200x004","69.9200x006","69.9200x007","69.9200x008","69.9202","75.9900x004"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合NG1入组条件，匹配规则：某一手术匹配')
    
    if MDCN_DRG.NG19_group(record):
      return 'NG19'

    return 'NG1'
  else:
    return ''

