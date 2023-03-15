from drg_group.tongchuan_2022.Base import message,intersect,SS_VALID
from drg_group.tongchuan_2022.DRG import MDCH_DRG

def group(record):
  adrg_zd=["K85.002","K85.102","K85.202","K85.302","K85.800x001","K85.800x002","K85.800x003","K85.813","K85.814","K85.815","K85.816","K85.817","K85.818","K85.821","K85.822","K85.902","K86.801"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合HT1入组条件，匹配规则：主诊断匹配')
    
    if MDCH_DRG.HT11_group(record):
      return 'HT11'

    if MDCH_DRG.HT13_group(record):
      return 'HT13'

    if MDCH_DRG.HT15_group(record):
      return 'HT15'

    return 'HT1'
  else:
    return ''

