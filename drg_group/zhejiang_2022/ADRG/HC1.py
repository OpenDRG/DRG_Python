from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCH_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["51.2100","51.2200","51.2200x004","51.2201","51.2300","51.2301","51.2400"]
  adrg_ss1=["51.1104","51.3601","51.3602","51.3903","51.3905","51.4100x001","51.4201","51.4202","51.5100","51.5101","51.5102","51.6301","51.6302","51.6303","51.6402","51.6900x012","51.7200x001","51.7201","51.7202","51.7203","51.7204","51.7900x006","51.8803","51.8807"]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and intersect(record.ssList,adrg_ss) and intersect(record.ssList,adrg_ss1):
    message('符合HC1入组条件，匹配规则：双手术匹配')
    
    if MDCH_DRG.HC11_group(record):
      return 'HC11'

    if MDCH_DRG.HC1B_group(record):
      return 'HC13'

    return ''
  else:
    return ''

