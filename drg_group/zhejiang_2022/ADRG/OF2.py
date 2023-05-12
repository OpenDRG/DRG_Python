from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCO_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["69.0100x002","69.0101","69.0200x003","69.0201","69.0902","69.5101","69.5102","69.5103","69.5202","69.5901","73.4x00x004","73.8x00x003","96.4902"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合OF2入组条件，匹配规则：主手术匹配')
    
    if MDCO_DRG.OF21_group(record):
      return 'OF21'

    if MDCO_DRG.OF23_group(record):
      return 'OF23'

    if MDCO_DRG.OF25_group(record):
      return 'OF25'

    return ''
  else:
    return ''

