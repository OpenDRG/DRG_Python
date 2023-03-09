from drg_group.fuzhou_2022.Base import message,intersect,SS_VALID
from drg_group.fuzhou_2022.DRG import MDCR_DRG

def group(record):
  adrg_zd=["Z51.101","Z51.102","Z51.103","Z51.104","Z51.200x008","Z51.500x001","Z51.500x002","Z51.800x094","Z51.800x095","Z51.800x096","Z51.800x922","Z51.800x924","Z51.800x925","Z51.800x927","Z51.800x951","Z51.800x952","Z51.800x981","Z51.801","Z51.802","Z51.804","Z51.805","Z51.807","Z51.808","Z51.809","Z51.810"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合RU1入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RU11_group(record):
      return 'RU11'

    if MDCR_DRG.RU13_group(record):
      return 'RU13'

    if MDCR_DRG.RU15_group(record):
      return 'RU15'

    return 'RU1'
  else:
    return ''

