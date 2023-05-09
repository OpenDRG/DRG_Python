from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["C50.200","C50.300","C50.400","C50.500","C50.801","C50.802","C50.803","C50.804","C50.900","C50.900x005","C50.902","C79.806","D05.100","D05.900","D17.100x002","D24.x00","D24.x02","D48.600x001","D48.601","L02.403","L72.105","L90.500x045","N60.000","N60.000x001","N60.100x003","N60.200","N60.201","N60.202","N60.300","N60.400","N60.801","N61.x00x014","N61.x01","N61.x03","N61.x04","N61.x05","N61.x06","N61.x07","N62.x00x004","N62.x02","N63.x00","N63.x01","N64.100","N64.504","N64.805","Q83.100","Q83.100x001","Q83.100x002","Q85.900x009","T85.400"]
  adrg_zd1=[]
  adrg_ss=["40.2200","85.0x00x002","85.0x01","85.0x02","85.2000x001","85.2000x002","85.2100x003","85.2100x019","85.2100x020","85.2100x021","85.2100x022","85.2101","85.2400x004","85.2400x005","85.2401","85.9900"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合JB3入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCJ_DRG.JB39_group(record):
      return 'JB39'

    return 'JB3'
  else:
    return ''

