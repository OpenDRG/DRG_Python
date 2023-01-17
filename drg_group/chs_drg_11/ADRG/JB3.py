from drg_group.chs_drg_11.Base import message,intersect,SS_VALID
from drg_group.chs_drg_11.DRG import MDCJ_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["40.1900x002","40.2200","85.0x00x002","85.0x00x003","85.0x01","85.0x02","85.2000x001","85.2000x002","85.2100x003","85.2100x019","85.2100x020","85.2100x021","85.2100x022","85.2101","85.2400x004","85.2400x005","85.2401","85.2402","85.2500","85.9900"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合JB3入组条件，匹配规则：主手术匹配')
    
    if MDCJ_DRG.JB39_group(record):
      return 'JB39'

    return 'JB3'
  else:
    return ''

