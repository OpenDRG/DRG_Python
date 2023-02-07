from drg_group.beijing_2022.Base import message,intersect,SS_VALID
from drg_group.beijing_2022.DRG import MDCR_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["92.2000","92.2001","92.2100","92.2700x002","92.2700x004","92.2701","92.2702","92.2703","92.2704","92.2705","92.2706","92.2800","92.2801","92.2900x002","92.2900x003"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合RC2入组条件，匹配规则：主手术匹配')
    
    if MDCR_DRG.RC22_group(record):
      return 'RC22'

    if MDCR_DRG.RC24_group(record):
      return 'RC24'

    if MDCR_DRG.RC26_group(record):
      return 'RC26'

    if MDCR_DRG.RC28_group(record):
      return 'RC28'

    return 'RC2'
  else:
    return ''

