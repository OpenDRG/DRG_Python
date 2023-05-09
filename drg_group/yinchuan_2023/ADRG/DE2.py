from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCD_DRG

def group(record):
  adrg_zd=["B44.200x001+J99.8*","D10.400","D10.900","D11.000","D18.000x510","G47.300","G47.300x001","G47.300x037","G47.301","H65.900x001","J01.900","J03.900","J03.901","J31.000","J31.001","J31.203","J35.000","J35.100","J35.200","J35.300","J35.803","J35.805","J35.901","J36.x00","J36.x00x003","J38.715","J39.215","R06.501","T17.200"]
  adrg_zd1=[]
  adrg_ss=["28.0x00x002","28.2x00x002","28.2x00x003","28.2x03","28.2x04","28.3x01","28.3x02","28.3x03","28.5x00","28.5x02","28.5x03","28.6x00x001","28.6x00x002","28.6x00x005","28.6x01","28.6x02","28.9201"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合DE2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCD_DRG.DE29_group(record):
      return 'DE29'

    return 'DE2'
  else:
    return ''

