from drg_group.chs_drg_10.Base import message,intersect,SS_VALID
from drg_group.chs_drg_10.DRG import MDCR_DRG

def group(record):
  adrg_zd=["Z51.101","Z51.102","Z51.103","Z51.104","Z51.200x008","Z51.500x002","Z51.800x095","Z51.800x922","Z51.800x951","Z51.800x952","Z51.800x981","Z51.801","Z51.807"]
  adrg_zd1=[]
  adrg_ss=["54.9701","54.9702","54.9703","99.2500x017","99.2500x036","99.2500x037","99.2500x038","99.2500x039","99.2503","99.2504","99.2505","99.2506","99.2800x004","99.2800x005","99.2800x006","99.2801"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss:
    message('符合RE1入组条件，匹配规则：主诊断匹配、主手术匹配')
    
    if MDCR_DRG.RE11_group(record):
      return 'RE11'

    if MDCR_DRG.RE13_group(record):
      return 'RE13'

    if MDCR_DRG.RE15_group(record):
      return 'RE15'

    return 'RE1'
  else:
    return ''

