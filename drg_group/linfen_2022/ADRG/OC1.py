from drg_group.linfen_2022.Base import message,intersect,SS_VALID
from drg_group.linfen_2022.DRG import MDCO_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["72.0x00","72.2100","72.2900x001","72.3100","72.3900x001","72.7100x001","73.5100","73.5900x001","73.5900x002","73.5900x003","73.6x00x002","73.6x01","73.6x02","73.8x00x002","73.8x00x003","73.8x00x005","73.8x00x006","73.8x01","73.8x02","73.9200","73.9300","73.9400","73.9900","75.4x00x001","75.4x00x002","75.4x00x003","75.6905","75.9100x001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合OC1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCO_DRG.OC13_group(record):
      return 'OC13'

    if MDCO_DRG.OC15_group(record):
      return 'OC15'

    return 'OC1'
  else:
    return ''

