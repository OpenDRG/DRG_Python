from drg_group.nanping_2023.Base import message,intersect,SS_VALID
from drg_group.nanping_2023.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["55.6100","55.6901"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合AE1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCA_DRG.AE19_group(record):
      return 'AE19'

    return 'AE1'
  else:
    return ''

