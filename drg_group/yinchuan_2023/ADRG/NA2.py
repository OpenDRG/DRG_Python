from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCN_DRG

def group(record):
  adrg_zd=["C45.100","C51.900","C52.x00","C53.000","C53.100","C53.900","C54.100","C54.200","C55.x00","C56.x00","C56.x00x003","C57.000","C57.000x002","C57.803","C57.900","C58.x00x002","C79.814","D06.000","D06.100","D06.900","D07.000","D07.100","D07.301","D39.000x002","D39.100x003","D39.200x001","D39.203"]
  adrg_zd1=[]
  adrg_ss=["54.4x00x005","54.4x12","65.2200","65.2501","65.2901","65.3100","65.3900x001","65.4100","65.4900x001","65.5100","65.5300","65.6100","65.6300","65.6400","66.4x02","66.5100","66.5102","66.6102","66.6104","68.2500x001","68.2912","68.3102","68.3901","68.4100","68.4901","69.1904","70.3301","70.3305","71.3x03","71.6200x002"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合NA2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCN_DRG.NA29_group(record):
      return 'NA29'

    return 'NA2'
  else:
    return ''

