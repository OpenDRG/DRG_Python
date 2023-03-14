from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["41.0100","41.0401","41.0701","41.0900"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合AG2入组条件，匹配规则：某一手术匹配')
    
    if MDCA_DRG.AG29_group(record):
      return 'AG29'

    return 'AG2'
  else:
    return ''

