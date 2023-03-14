from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["31.1x00x005","31.2100x001","31.2900x001","39.6500","96.0400","96.7201"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合AH1入组条件，匹配规则：某一手术匹配')
    
    if MDCA_DRG.AH11_group(record):
      return 'AH11'

    if MDCA_DRG.AH13_group(record):
      return 'AH13'

    if MDCA_DRG.AH19_group(record):
      return 'AH19'

    return 'AH1'
  else:
    return ''

