from drg_group.qingdao_2023.Base import message,intersect,SS_VALID
from drg_group.qingdao_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["38.0900x003","38.5900x005","38.5900x008","38.5900x009","38.5900x010","38.5901","38.5902","38.5903","38.5904","38.5905","38.5906","38.5907","39.2900x001","39.2900x002","39.2900x044"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FF1入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FF19_group(record):
      return 'FF19'

    return 'FF1'
  else:
    return ''

