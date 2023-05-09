from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["Q20.100","Q20.302","Q20.400","Q21.000","Q21.100","Q21.101","Q21.102","Q21.104","Q21.105","Q21.200","Q21.205","Q21.800","Q21.804","Q21.900","Q22.100","Q22.500","Q22.600","Q22.900","Q23.101","Q23.900x001","Q23.901","Q24.501","Q24.502","Q24.507","Q24.508","Q24.511","Q24.800x012","Q24.806","Q24.810","Q24.900","Q25.000","Q25.100","Q25.300","Q25.404","Q25.407","Q25.408","Q25.500","Q25.600","Q25.704","Q26.500x001","Q26.800x001","Q26.800x008","Q87.400"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合FV1入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FV19_group(record):
      return 'FV19'

    return 'FV1'
  else:
    return ''

