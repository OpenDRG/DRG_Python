from drg_group.xian_2020.Base import message,intersect,SS_VALID
from drg_group.xian_2020.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["20.7100","20.7903","38.0700x001","38.0701","38.5701","38.7x00x010","38.8700x010","38.9900x002","38.9900x501","38.9900x701","38.9900x901","39.3201","44.4400x001","55.9902","99.1000x011"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FF4入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FF49_group(record):
      return 'FF49'

    return 'FF4'
  else:
    return ''

