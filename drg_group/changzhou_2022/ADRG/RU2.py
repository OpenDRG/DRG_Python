from drg_group.changzhou_2022.Base import message,intersect,SS_VALID
from drg_group.changzhou_2022.DRG import MDCR_DRG

def group(record):
  adrg_zd=["Z51.800x095","Z51.800x951","Z51.800x952","Z51.802","Z51.805","Z51.808","Z51.810"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合RU2入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RU29_group(record):
      return 'RU29'

    return 'RU2'
  else:
    return ''

