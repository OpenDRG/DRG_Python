from drg_group.wlmq_2022.Base import message,intersect,SS_VALID
from drg_group.wlmq_2022.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["41.0000","41.0200","41.0300","41.0500","41.0600","41.0800x001"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合AG1入组条件，匹配规则：主手术匹配')
    
    if MDCA_DRG.AG19_group(record):
      return 'AG19'

    return 'AG1'
  else:
    return ''

