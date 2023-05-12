from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["52.8000","52.8200","52.8300","55.6100","55.6901"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合AC1入组条件，匹配规则：主手术匹配')
    
    if MDCA_DRG.AC19_group(record):
      return 'AC19'

    return ''
  else:
    return ''

