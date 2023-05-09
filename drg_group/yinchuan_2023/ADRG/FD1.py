from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I08.006","I42.100","I42.200x002","I45.600","I48.100","Q21.000","Q21.100","Q21.101","Q21.102","Q21.104","Q21.105","Q21.200","Q21.805","Q24.200","Q25.000","Q25.408","Q26.400"]
  adrg_zd1=[]
  adrg_ss=["35.3400x003","35.3901","35.4200x002","35.4200x008","35.5100x001","35.5100x002","35.5300x001","35.5300x003","35.6100x001","35.6101","35.6102","35.6201","35.6300x003","35.7100x002","35.7100x009","35.7100x010","35.7101","35.7200x001","35.7300x002","35.7300x004","35.8100x003","35.8201","37.3300x009","37.3300x020","37.3501","38.8500x012","38.8505"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FD1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FD19_group(record):
      return 'FD19'

    return 'FD1'
  else:
    return ''

