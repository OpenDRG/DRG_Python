from drg_group.beijing_2022.Base import message,intersect,SS_VALID
from drg_group.beijing_2022.DRG import MDCH_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["51.3903","51.3905","51.4100x001","51.4201","51.4202","51.4301","51.4302","51.4303","51.4304","51.4900x002","51.4900x003","51.4901","51.4902","51.4903","51.4904","51.4905","51.5100","51.5101","51.5102","51.6100x001","51.6101","51.6300x001","51.6301","51.6302","51.6303","51.7101","51.7200x001","51.7201","51.7202","51.7203","51.7204","51.7900x006","51.8701","51.8800x006","51.8800x009","51.8801","51.8802","51.8803","51.8804","51.8805","51.8806","51.8807"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合HC1入组条件，匹配规则：主手术匹配')
    
    if MDCH_DRG.HC11_group(record):
      return 'HC11'

    if MDCH_DRG.HC13_group(record):
      return 'HC13'

    if MDCH_DRG.HC15_group(record):
      return 'HC15'

    return 'HC1'
  else:
    return ''

