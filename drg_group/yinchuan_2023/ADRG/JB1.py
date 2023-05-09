from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["C50.200","C50.300","C50.400","C50.500","C50.801","C50.803","C50.804","C50.900","D24.x00","N60.201","N61.x00x014","N61.x03","N61.x04","N61.x05","N61.x06","N62.x00x001","N62.x02","T85.400","T85.401"]
  adrg_zd1=[]
  adrg_ss=["85.3100","85.3200","85.3500x001","85.6x00x001","85.7000x001","85.7100x001","85.7400x001","85.7900x001","85.8400","85.8701","85.8900x005","85.9100","85.9300","85.9400"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合JB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCJ_DRG.JB19_group(record):
      return 'JB19'

    return 'JB1'
  else:
    return ''

