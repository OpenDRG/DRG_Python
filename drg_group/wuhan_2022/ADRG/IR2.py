from drg_group.wuhan_2022.Base import message,intersect,SS_VALID
from drg_group.wuhan_2022.DRG import MDCI_DRG

def group(record):
  adrg_zd=["S72.000","S72.000x011","S72.000x021","S72.000x031","S72.000x041","S72.000x051","S72.000x081","S72.000x082","S72.010","S72.100x001","S72.100x002","S72.101","S72.110","S72.200x001","S72.210","S72.910"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合IR2入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IR21_group(record):
      return 'IR21'

    if MDCI_DRG.IR2B_group(record):
      return 'IR2B'

    return 'IR2'
  else:
    return ''

