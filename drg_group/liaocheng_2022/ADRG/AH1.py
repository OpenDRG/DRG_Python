from drg_group.liaocheng_2022.Base import message,intersect,SS_VALID
from drg_group.liaocheng_2022.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["37.5200x001","39.6500","96.7201"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合AH1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCA_DRG.AH15_group(record):
      return 'AH15'

    if MDCA_DRG.AH11_group(record):
      return 'AH11'

    return 'AH1'
  else:
    return ''

