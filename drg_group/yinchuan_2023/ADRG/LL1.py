from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["E10.200x215+N08.3*","E10.201+N08.3*","E11.200x214+N08.3*","E11.200x215+N08.3*","E11.201+N08.3*","M31.701+N08.5*","N01.900x001","N03.100","N03.901","N04.101","N17.900","N17.900x003","N18.400","N18.500","N18.902","Z49.101","Z49.201"]
  adrg_zd1=[]
  adrg_ss=["39.9500x007","39.9501","39.9600x003","54.9800x008"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合LL1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCL_DRG.LL11_group(record):
      return 'LL11'

    if MDCL_DRG.LL15_group(record):
      return 'LL15'

    return 'LL1'
  else:
    return ''

