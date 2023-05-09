from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCD_DRG

def group(record):
  adrg_zd=["D18.000x506","D18.001","D18.003","D22.200x002","D22.201","D23.200x002","D23.200x003","D23.201","D36.702","H60.000x002","H60.300","H60.400","H60.400x004","H60.401","H60.901","H61.000","H61.100x002","H61.100x009","H61.102","H61.103","H61.105","H61.200","H61.803","H61.804","H61.806","H61.901","H65.900x001","H66.301","H66.400","H70.001","H73.001","H81.000","H90.801","H93.901","J01.900","J06.000","Q17.000","Q17.200","Q17.900","Q18.102","Q18.104","S01.300x012","T16.x00x001","Z42.000x015"]
  adrg_zd1=[]
  adrg_ss=["18.0200x003","18.0201","18.0202","18.0900x002","18.0901","18.0902","18.2100x006","18.2101","18.2900x003","18.2900x009","18.2900x016","18.2900x017","18.2901","18.2907","18.6x00x001","18.6x01","18.6x02","18.7100x001","18.7100x002","18.7105","18.7901","18.7905","18.7906","18.9x00x007","20.0902"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合DC2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCD_DRG.DC29_group(record):
      return 'DC29'

    return 'DC2'
  else:
    return ''

