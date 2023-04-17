from drg_group.lanzhou_2023.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2023.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["37.5200x001","39.6500","96.7201"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合AH1入组条件，匹配规则：主手术匹配')
    
    if MDCA_DRG.AH11_group(record):
      return 'AH11'

    if MDCA_DRG.AH1B_group(record):
      return 'AH14'

    return 'AH1'
  else:
    return ''

