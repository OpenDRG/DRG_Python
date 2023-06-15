from drg_group.yunnan_2022.Base import message,intersect,SS_VALID
from drg_group.yunnan_2022.DRG import MDCC_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["08.5200","08.8600","09.4300x001","09.4900x004","09.4900x005","09.8100","09.8100x004","09.8101","09.8300x001","09.9900x003","09.9900x004","10.1x00x003","10.9100","10.9900x004","11.3100x001","11.9900x003","11.9900x004","11.9900x005","12.0100","12.0200x002","12.0200x004","15.7x00","16.0200","16.1x00x001","16.7200x002","16.9100","16.9100x001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合CJ1入组条件，匹配规则：主手术匹配')
    
    
    if MDCC_DRG.CJ19_group(record):
      return 'CJ19'

    return ''
  else:
    return ''
