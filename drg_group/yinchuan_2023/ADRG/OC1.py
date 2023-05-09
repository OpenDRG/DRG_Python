from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCO_DRG

def group(record):
  adrg_zd=["O03.601","O04.902","O10.900x001","O11.x01","O13.x01","O14.000x001","O14.900","O24.400","O32.401","O32.601","O34.201","O34.802","O35.800x003","O36.302","O36.401","O41.000","O41.100","O42.000x001","O42.000x002","O42.100x011","O42.100x012","O42.900","O43.105","O45.900","O69.101","O69.208","O72.001","O72.100","O72.101","O72.202","O73.102","O99.005","O99.215"]
  adrg_zd1=[]
  adrg_ss=["73.5900x002","73.6x01","75.4x00x001","75.4x00x002","75.6905"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合OC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCO_DRG.OC19_group(record):
      return 'OC19'

    return 'OC1'
  else:
    return ''

