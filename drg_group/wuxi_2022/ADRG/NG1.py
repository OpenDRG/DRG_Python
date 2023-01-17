from drg_group.wuxi_2022.Base import message,intersect,SS_VALID
from drg_group.wuxi_2022.DRG import MDCN_DRG

def group(record):
  adrg_zd=["N96.x00x003","N97.000x001","N97.100x001","N97.100x003","N97.101","N97.200x001","N97.200x002","N97.300","N97.800x004","N97.801","N97.900","N97.901","N97.902","Z31.100","Z31.200","Z31.200x003","Z31.201","Z31.300x001","Z31.300x002"]
  adrg_zd1=[]
  adrg_ss=["65.9900x008","69.9200x004","69.9200x006","69.9200x007","69.9200x008","69.9201","69.9202"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss:
    message('符合NG1入组条件，匹配规则：主诊断匹配、主手术匹配')
    
  return ''

