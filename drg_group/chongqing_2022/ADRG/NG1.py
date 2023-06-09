from drg_group.chongqing_2022.Base import message,intersect,SS_VALID
from drg_group.chongqing_2022.DRG import MDCN_DRG

def group(record):
  adrg_zd=["Z31.100","Z31.200","Z31.200x003","Z31.201","Z31.300x001","Z31.300x002"]
  adrg_zd1=[]
  adrg_ss=["65.9900x005","65.9900x006","65.9900x008","69.9200x004","69.9200x006","69.9200x007","69.9200x008","69.9201","69.9202","75.9900x004"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss:
    message('符合NG1入组条件，匹配规则：主诊断匹配、主手术匹配')
    
    
    if MDCN_DRG.NG11_group(record):
      return 'NG11'

    if MDCN_DRG.NG13_group(record):
      return 'NG13'

    if MDCN_DRG.NG15_group(record):
      return 'NG15'

    return ''
  else:
    return ''
