from drg_group.yunnan_2023.Base import message,intersect,SS_VALID
from drg_group.yunnan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["35.4200x003","35.4200x009","35.5200x001","35.5200x002","35.5201","35.5500x001","35.9800x001","35.9800x002","36.9900x005","39.7800x008","39.7900x402"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FD3入组条件，匹配规则：主手术匹配')
    
    
    if MDCF_DRG.FD39_group(record):
      return 'FD39'

    return ''
  else:
    return ''
