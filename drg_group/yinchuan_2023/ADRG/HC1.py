from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=["C22.000","C24.000x007","C24.002","C24.003","C24.100","C25.000","C25.900","K75.003","K80.000x004","K80.002","K80.100x001","K80.201","K80.300x005","K80.301","K80.302","K80.303","K80.304","K80.305","K80.306","K80.402","K80.404","K80.500x002","K80.501","K80.503","K80.504","K80.505","K80.801","K83.001","K83.005","K83.019","K83.103","K83.105","K83.109","K83.502","K83.807","K85.100","K85.101","K85.102","K85.900","K86.100x002","Q44.400","Q44.504"]
  adrg_zd1=[]
  adrg_ss=["51.4100x001","51.4303","51.4304","51.4900x002","51.4902","51.4903","51.5100","51.5101","51.6100x001","51.6300x001","51.6301","51.6302","51.6303","51.7200x001","51.7202","51.7203","51.8701","51.8800x006","51.8800x009","51.8801","51.8802","51.8803","51.8804","51.8805","51.8806","51.8807"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合HC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCH_DRG.HC11_group(record):
      return 'HC11'

    if MDCH_DRG.HC15_group(record):
      return 'HC15'

    return 'HC1'
  else:
    return ''

