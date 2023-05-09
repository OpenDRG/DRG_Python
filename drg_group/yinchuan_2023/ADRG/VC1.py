from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCV_DRG

def group(record):
  adrg_zd=["S41.800x001","S51.000","S61.000x001","S61.100x001","S61.100x002","S61.800x012","S61.900x002","S68.100x002","S69.900x002","S69.900x004","S71.100","S81.000","S81.700","S81.800x083","S81.900","S91.000","S91.300x002","S91.300x003","T01.200x001","T01.300x001","T01.902","T01.903","T13.100","T54.202","T75.400x001","T81.024","T81.301","T81.800x001","T81.800x017","T81.808","T81.811","T81.812","T81.813","T85.700","T98.200x033"]
  adrg_zd1=[]
  adrg_ss=["79.6302","79.6400","79.6601","83.4501","86.2200x011","86.2201","86.2800x012"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合VC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCV_DRG.VC13_group(record):
      return 'VC13'

    if MDCV_DRG.VC15_group(record):
      return 'VC15'

    return 'VC1'
  else:
    return ''

