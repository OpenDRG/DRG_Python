from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["M84.100","S32.300","S32.400","S32.500x002","S32.500x003","S32.700","S32.701","S32.801","S32.802"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合IR1入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IR19_group(record):
      return 'IR19'

    return 'IR1'
  else:
    return ''

