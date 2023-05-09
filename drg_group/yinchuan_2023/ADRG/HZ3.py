from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=["A18.817+K87.1*","D13.600","D37.700x003","D37.705","D37.706","K86.000","K86.100x002","K86.100x004","K86.101","K86.103","K86.200","K86.300","K86.800x002","K86.806","K86.808","K86.809","K86.810","K86.812","K86.815","K86.817","K86.901","Q45.100","Q45.301","Q45.802","R93.302","S36.200x001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合HZ3入组条件，匹配规则：主诊断匹配')
    
    if MDCH_DRG.HZ31_group(record):
      return 'HZ31'

    if MDCH_DRG.HZ35_group(record):
      return 'HZ35'

    return 'HZ3'
  else:
    return ''

