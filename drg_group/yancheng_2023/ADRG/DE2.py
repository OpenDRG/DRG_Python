from drg_group.yancheng_2023.Base import message,intersect,SS_VALID
from drg_group.yancheng_2023.DRG import MDCD_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["28.0x00x002","28.0x02","28.2x00x002","28.2x00x003","28.2x01","28.2x02","28.2x03","28.2x04","28.3x01","28.3x02","28.3x03","28.4x00","28.5x00","28.5x01","28.5x02","28.5x03","28.6x00x001","28.6x00x002","28.6x00x004","28.6x00x005","28.6x01","28.6x02","28.6x03","28.7x01","28.7x02","28.9200x002","28.9201","28.9202","28.9900"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合DE2入组条件，匹配规则：主手术匹配')
    
    if MDCD_DRG.DE29_group(record):
      return 'DE29'

    return 'DE2'
  else:
    return ''

