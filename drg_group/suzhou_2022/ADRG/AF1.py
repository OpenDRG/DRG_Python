from drg_group.suzhou_2022.Base import message,intersect,SS_VALID
from drg_group.suzhou_2022.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["33.5000","33.5100","33.5200","33.6x00"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合AF1入组条件，匹配规则：主手术匹配')
    
    if MDCA_DRG.AF19_group(record):
      return 'AF19'

  return ''

