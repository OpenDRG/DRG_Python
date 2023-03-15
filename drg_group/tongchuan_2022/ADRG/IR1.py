from drg_group.tongchuan_2022.Base import message,intersect,SS_VALID
from drg_group.tongchuan_2022.DRG import MDCI_DRG

def group(record):
  adrg_zd=["M84.000x052","M84.100","M84.100x052","S32.300","S32.310","S32.400","S32.410","S32.500x002","S32.500x003","S32.510","S32.700","S32.701","S32.800x091","S32.800x092","S32.800x093","S32.800x094","S32.800x095","S32.801","S32.802","S32.811","S32.812"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合IR1入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IR19_group(record):
      return 'IR19'

    return 'IR1'
  else:
    return ''

