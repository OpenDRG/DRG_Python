from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["C50.000x001","C50.001","C50.100","C50.200","C50.300","C50.400","C50.500","C50.801","C50.802","C50.803","C50.804","C50.900","C50.900x005","C50.901","C50.902","D05.100","D05.900","D24.x00","D48.600x001","D48.601","N60.000","N60.000x001","N60.101","N60.200","N60.201","N60.202","N60.300","N60.400","N61.x01","N61.x03","N61.x04","N61.x06","N61.x07","N62.x02","N63.x00","N64.501","Q85.900x009"]
  adrg_zd1=[]
  adrg_ss=["40.5000","40.5100","85.2200","85.2300x001","85.2301","85.2400x006","85.3400x002","85.3401","85.3601","85.4100x001","85.4200x001","85.4300x003","85.4301","85.4302","85.4303","85.4401","85.4500","85.4500x001","85.4500x003","85.4501","85.4600","85.4700"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合JB2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCJ_DRG.JB29_group(record):
      return 'JB29'

    return 'JB2'
  else:
    return ''

