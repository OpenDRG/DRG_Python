from drg_group.yunnan_2022.Base import message,intersect,SS_VALID
from drg_group.yunnan_2022.DRG import MDCR_DRG

def group(record):
  adrg_zd=["Z51.000x013","Z51.100x004","Z51.500x003","Z51.800x953","Z51.800x983"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合RW2入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RW29_group(record):
      return 'RW29'

    return 'RW2'
  else:
    return ''

