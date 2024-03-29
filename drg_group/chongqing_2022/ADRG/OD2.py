from drg_group.chongqing_2022.Base import message,intersect,SS_VALID
from drg_group.chongqing_2022.DRG import MDCO_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["66.8x03","67.0x01","67.3100","67.3200","67.3200x009","67.3200x012","67.3201","67.3202","67.3300","67.3301","67.3302","67.3904","67.5900x002","67.5900x003","68.2917","70.1200x001","70.1300","70.1400x007","70.1405","70.1406","70.1407","70.1408","71.2200x001","71.2200x002","71.2400x001","71.2400x003","71.2900x002","71.3x00x001","71.3x00x007","71.3x00x011","71.3x01","71.3x04","75.8x00x002","75.9201","75.9202","75.9900x006"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合OD2入组条件，匹配规则：主手术匹配')
    
    
    if MDCO_DRG.OD29_group(record):
      return 'OD29'

    return ''
  else:
    return ''
