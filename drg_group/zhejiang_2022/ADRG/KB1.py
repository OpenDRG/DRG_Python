from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCK_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["07.0000","07.0100","07.0200","07.1200","07.1200x003","07.2100","07.2101","07.2102","07.2103","07.2200","07.2201","07.2900x001","07.2900x003","07.2901","07.2902","07.3x00","07.3x01","07.4101","07.4102","07.4103","07.4200","07.4300","07.4400","07.4501","07.4900"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合KB1入组条件，匹配规则：某一手术匹配')
    
    if MDCK_DRG.KB11_group(record):
      return 'KB11'

    if MDCK_DRG.KB13_group(record):
      return 'KB13'

    if MDCK_DRG.KB15_group(record):
      return 'KB15'

    return 'KB1'
  else:
    return ''

