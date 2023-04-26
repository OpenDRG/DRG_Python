from drg_group.qingdao_2023.Base import message,intersect,SS_VALID
from drg_group.qingdao_2023.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["39.6500"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合AH1_2入组条件，匹配规则：某一手术匹配')
    
    if MDCA_DRG.AH19_group(record):
      return 'AH19'

    return 'AH1'
  else:
    return ''

