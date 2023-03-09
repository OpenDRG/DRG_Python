from drg_group.fuzhou_2022.Base import message,intersect,SS_VALID
from drg_group.fuzhou_2022.DRG import MDCG_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["47.0100","47.0901","47.0902","47.0903","47.1100","47.1900x001","47.2x00","47.2x01","47.9100","47.9200","47.9901"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合GD2入组条件，匹配规则：主手术匹配')
    
    if MDCG_DRG.GD23_group(record):
      return 'GD23'

    if MDCG_DRG.GD25_group(record):
      return 'GD25'

    return 'GD2'
  else:
    return ''

