from drg_group.guangxi_2022.Base import message,intersect,SS_VALID
from drg_group.guangxi_2022.DRG import MDCJ_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["40.5000","40.5100","40.5101","85.2100x023","85.2200","85.2300x001","85.2301","85.2400x006","85.3400x002","85.3401","85.3600x001","85.3601","85.4100x001","85.4200x001","85.4200x003","85.4300x003","85.4301","85.4302","85.4303","85.4401","85.4402","85.4403","85.4500","85.4500x001","85.4500x003","85.4501","85.4600","85.4700","85.4800"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合JB2入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCJ_DRG.JB23_group(record):
      return 'JB23'

    if MDCJ_DRG.JB25_group(record):
      return 'JB25'

    return 'JB2'
  else:
    return ''

