from drg_group.chs_drg_11.Base import message,intersect,SS_VALID
from drg_group.chs_drg_11.DRG import MDCR_DRG

def group(record):
  adrg_zd=["Z51.000x013","Z51.100x004","Z51.500x003","Z51.800x953","Z51.800x983"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合RW2入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RW21_group(record):
      return 'RW21'

    if MDCR_DRG.RW23_group(record):
      return 'RW23'

    if MDCR_DRG.RW25_group(record):
      return 'RW25'

    return 'RW2'
  else:
    return ''

