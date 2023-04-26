from drg_group.qingdao_2023.Base import message,intersect,SS_VALID
from drg_group.qingdao_2023.DRG import MDCK_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["07.1300","07.1400","07.1500","07.5100x001","07.5200x001","07.5300","07.5301","07.5400x001","07.6100x002","07.6100x003","07.6100x004","07.6200x003","07.6200x007","07.6201","07.6202","07.6301","07.6400x001","07.6500","07.6501","07.6800","07.6900x001","07.7100","07.7200x002","07.7200x003","07.7201","07.7202","07.7203","07.7901"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合KC1入组条件，匹配规则：主手术匹配')
    
    if MDCK_DRG.KC19_group(record):
      return 'KC19'

    return 'KC1'
  else:
    return ''

