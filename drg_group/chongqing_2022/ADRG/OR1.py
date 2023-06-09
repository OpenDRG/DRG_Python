from drg_group.chongqing_2022.Base import message,intersect,SS_VALID
from drg_group.chongqing_2022.DRG import MDCO_DRG

def group(record):
  adrg_zd=["O75.700x001","O80.000","O80.100","O80.800","O80.900","O84.000"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合OR1入组条件，匹配规则：主诊断匹配')
    
    
    if MDCO_DRG.OR19_group(record):
      return 'OR19'

    return ''
  else:
    return ''
