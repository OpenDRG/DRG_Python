from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=["K75.805","K75.806","K80.000x002","K80.000x004","K80.001","K80.002","K80.100x001","K80.200x001","K80.200x003","K80.201","K80.300x002","K80.300x005","K80.301","K80.302","K80.303","K80.304","K80.305","K80.306","K80.401","K80.402","K80.405","K80.500x002","K80.501","K80.502","K80.503","K80.504","K80.801","K81.000","K81.002","K81.003","K81.004","K81.006","K81.007","K81.900","K82.200","K82.200x002","K83.000","K83.000x007","K83.000x012","K83.001","K83.005","K83.008","K83.009","K83.010","K83.012","K83.013","K83.019","K83.100","K83.109"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合HU1入组条件，匹配规则：主诊断匹配')
    
    if MDCH_DRG.HU11_group(record):
      return 'HU11'

    if MDCH_DRG.HU13_group(record):
      return 'HU13'

    if MDCH_DRG.HU15_group(record):
      return 'HU15'

    return 'HU1'
  else:
    return ''

