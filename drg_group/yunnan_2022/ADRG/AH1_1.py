from drg_group.yunnan_2022.Base import message,intersect,SS_VALID
from drg_group.yunnan_2022.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=["Z93.000"]
  adrg_ss=["96.7201"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and intersect(record.zdList[1:],adrg_zd1) and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合AH1_1入组条件，匹配规则：其他诊断匹配、某一手术匹配')
    
    if MDCA_DRG.AH11_group(record):
      return 'AH11'

    if MDCA_DRG.AH15_group(record):
      return 'AH15'

    return 'AH1'
  else:
    return ''

