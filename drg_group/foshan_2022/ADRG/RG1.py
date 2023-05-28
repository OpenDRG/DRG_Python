from drg_group.foshan_2022.Base import message,intersect,SS_VALID
from drg_group.foshan_2022.DRG import MDCR_DRG
from drg_group.foshan_2022.DRG_EX import RG11,RG12,RG13,RG14

def group(record):
  adrg_zd=["Z51.800x095","Z51.800x951","Z51.800x952","Z51.800x981","Z51.801","Z51.805","Z51.807","Z51.810"]
  adrg_zd1=[]
  adrg_ss=["99.2800x004","99.2800x005","99.2800x006","99.2801"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合RG1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if RG11.group(record):
      return 'RG11'

    if RG12.group(record):
      return 'RG12'

    if RG13.group(record):
      return 'RG13'

    if RG14.group(record):
      return 'RG14'

    
    return ''
  else:
    return ''

