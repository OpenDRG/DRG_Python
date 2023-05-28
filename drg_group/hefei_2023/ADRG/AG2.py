from drg_group.hefei_2023.Base import message,intersect,SS_VALID
from drg_group.hefei_2023.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["41.0100","41.0401","41.0701","41.0900"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合AG2入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    
    if MDCA_DRG.AG21_group(record):
      return 'AG21'

    if MDCA_DRG.AG23_group(record):
      return 'AG23'

    if MDCA_DRG.AG25_group(record):
      return 'AG25'

    return ''
  else:
    return ''

