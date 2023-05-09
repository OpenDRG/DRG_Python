from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCG_DRG

def group(record):
  adrg_zd=["C15.400","C15.500","C15.801","C16.000","C16.001","C16.100","C16.200","C16.301","C16.500","C16.802","C16.900","C18.200","C18.700","C18.900","C20.x00","D00.100","D00.200","D01.000","D12.200","D12.600","D12.602","D12.800","D13.000","D13.100","D13.101","D13.200","D17.500x003","D17.500x008","D37.100x001","D37.100x002","D37.101","D37.103","D37.200x001","D37.401","D37.409","D37.500x001","K20.x00x001","K21.001","K22.600x001","K22.812","K25.900x001","K29.400","K29.603","K31.703","K31.902","K31.905","K44.901","K52.802","K62.100","K62.903","K63.500","K63.500x084","K63.501","K63.502","K63.503","K63.504","K63.801","K63.807","K63.813","K63.816","K63.900x001","Q45.300x104","R93.303"]
  adrg_zd1=[]
  adrg_ss=["43.4107","45.3004","45.3400x002","45.3400x005","45.4300x009","48.3600x003"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GK1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCG_DRG.GK19_group(record):
      return 'GK19'

    return 'GK1'
  else:
    return ''

