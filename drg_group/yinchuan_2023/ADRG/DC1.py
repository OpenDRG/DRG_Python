from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCD_DRG

def group(record):
  adrg_zd=["D17.000x003","D23.200x008","H60.400","H60.400x004","H60.401","H65.900x001","H66.000","H66.301","H66.400","H66.900","H66.900x003","H70.001","H70.100","H71.x00","H71.x01","H71.x04","H72.001","H72.900","H74.000","H74.101","H74.802","H80.900","H81.000","H90.200","H90.300","H93.901","H95.000x001","Q16.400","S09.200"]
  adrg_zd1=[]
  adrg_ss=["19.0x00x003","19.1900x006","19.2901","19.3x00x001","19.3x00x002","19.3x01","19.3x03","19.3x04","19.4x00x002","19.4x00x004","19.4x00x005","19.4x01","19.5200","19.5300","19.5400","19.6x00x001","19.9x01","20.0100x005","20.0100x006","20.2300x001","20.2300x002","20.2301","20.2303","20.4200x002","20.4900x007","20.4900x008","20.4900x009","20.4901","20.5100","20.5100x002","20.5100x003","20.6100x004","20.6200x002","20.8x02","20.8x05","20.9303"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合DC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCD_DRG.DC19_group(record):
      return 'DC19'

    return 'DC1'
  else:
    return ''

