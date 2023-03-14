from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["52.8000","52.8200","52.8300"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合AD1入组条件，匹配规则：某一手术匹配')
    
    if MDCA_DRG.AD19_group(record):
      return 'AD19'

    return 'AD1'
  else:
    return ''

