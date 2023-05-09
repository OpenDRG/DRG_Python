from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=["D37.601","D37.603","K80.101","K80.404","K81.100","K81.101","K82.305","K82.400","K82.802","K82.803","K82.900x001","K82.900x002","K83.006","K83.101","K83.102","K83.105","K83.107","K83.300","K83.302","K83.501","K83.502","K83.800x012","K83.805","K83.807","K83.817","K83.820","K83.901","K83.902","K91.500","K91.800x407","K91.807","Q44.101","Q44.200","Q44.301","Q44.400","Q44.505","R93.204","R93.205","S36.101"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合HZ2入组条件，匹配规则：主诊断匹配')
    
    if MDCH_DRG.HZ21_group(record):
      return 'HZ21'

    if MDCH_DRG.HZ23_group(record):
      return 'HZ23'

    if MDCH_DRG.HZ25_group(record):
      return 'HZ25'

    return 'HZ2'
  else:
    return ''

