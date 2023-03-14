from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCJ_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["40.2200","40.5000","40.5100","40.5101","85.4300x003","85.4301","85.4302","85.4303","85.4401","85.4402","85.4403","85.4500x001","85.4500x003","85.4501","85.4600","85.4700","85.4800"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合JA2入组条件，匹配规则：某一手术匹配')
    
    if MDCJ_DRG.JA21_group(record):
      return 'JA21'

    if MDCJ_DRG.JA23_group(record):
      return 'JA23'

    if MDCJ_DRG.JA25_group(record):
      return 'JA25'

    return 'JA2'
  else:
    return ''

