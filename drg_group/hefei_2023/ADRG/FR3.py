from drg_group.hefei_2023.Base import message,intersect,SS_VALID
from drg_group.hefei_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I20.000","I20.000x004","I20.000x005","I20.001","I20.002","I20.003","I20.004","I20.005","I20.006","I20.101","I20.102","I20.800x006","I20.800x007","I20.801","I20.802","I20.803","I20.806","I20.807","I20.808","I20.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合FR3入组条件，匹配规则：主诊断匹配')
    
    
    if MDCF_DRG.FR33_group(record):
      return 'FR33'

    if MDCF_DRG.FR35_group(record):
      return 'FR35'

    return ''
  else:
    return ''

