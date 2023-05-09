from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I20.000","I20.800x007","I20.801","I21.001","I21.003","I21.004","I21.103","I21.104","I21.106","I21.200x003","I21.200x019","I21.200x021","I21.200x023","I21.200x027","I21.200x029","I21.204","I21.208","I21.212","I21.300x004","I21.401","I21.900","I22.000x001","I22.800x009","I23.200x001","I24.901","I25.103","I25.500","I25.800x010","I44.102","I44.200","I45.502","I50.100x006","I50.900x018"]
  adrg_zd1=[]
  adrg_ss=["00.6600x004","00.6601","17.5500x002","17.5500x003","17.5501","36.0400","36.3400","37.6101","37.7800"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FM2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FM29_group(record):
      return 'FM29'

    return 'FM2'
  else:
    return ''

