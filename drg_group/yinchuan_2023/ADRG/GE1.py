from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCG_DRG

def group(record):
  adrg_zd=["K40.200x001","K40.201","K40.202","K40.204","K40.303","K40.304","K40.305","K40.306","K40.307","K40.309","K40.312","K40.313","K40.314","K40.315","K40.900x002","K40.900x003","K40.900x004","K40.900x005","K40.900x006","K40.901","K40.902","K40.903","K40.904","K40.905","K40.906","K41.200x001","K41.300x003","K41.302","K41.900x001","K42.000x001","K42.001","K42.900","K43.200","K43.500","K43.603","K46.000x002","K56.201","K56.700","K65.001","Q79.200"]
  adrg_zd1=[]
  adrg_ss=["17.1100x001","17.1200x001","17.1300x001","17.2100x001","17.2200x001","17.2300x001","17.2400x001","53.0001","53.0002","53.0100x001","53.0101","53.0102","53.0201","53.0202","53.0203","53.0204","53.0301","53.0302","53.0401","53.0501","53.1000","53.1101","53.1200x001","53.1201","53.1202","53.1203","53.1401","53.1501","53.1601","53.1701","53.2100x001","53.2101","53.2901","53.3100x001","53.4101","53.4201","53.4301","53.4901","53.5100","53.5101","53.5900x001","53.5901","53.5902","53.6101","53.6301","53.6302","53.6900x002","53.6901","53.9x00x015","53.9x00x019"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GE1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCG_DRG.GE13_group(record):
      return 'GE13'

    if MDCG_DRG.GE15_group(record):
      return 'GE15'

    return 'GE1'
  else:
    return ''

