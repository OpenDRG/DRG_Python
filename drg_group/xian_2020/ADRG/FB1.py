from drg_group.xian_2020.Base import message,intersect,SS_VALID
from drg_group.xian_2020.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["37.5200x001","37.5300x001","37.5400","37.5500","37.6000","37.6101","37.6200x002","37.6201","37.6301","37.6400x001","37.6500x001","37.6600x001","37.6600x002","37.6700","37.6800x001","37.6800x002","37.6800x003","37.6800x004","37.6800x005","39.6500"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FB1入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FB19_group(record):
      return 'FB19'

    return 'FB1'
  else:
    return ''

