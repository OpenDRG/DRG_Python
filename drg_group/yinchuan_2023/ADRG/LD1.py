from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["C66.x00","C67.600","D09.000","D30.300","D30.301","D41.400x004","D41.401","N13.202","N13.203","N18.400","N18.500","N20.000","N20.100","N21.000","N21.100","N28.100","N28.828","N30.201","N30.400","N30.800x004","N30.805","N30.807","N30.808","N30.809","N30.900","N32.000","N32.001","N32.802","N32.901","N35.900","N36.100","N36.804","N39.000","N39.300","N99.800x011","Q64.401","Q64.402","Q64.403","R31.x00","R93.405","T19.000","T83.802"]
  adrg_zd1=[]
  adrg_ss=["56.4103","57.0x00x002","57.0x00x005","57.0x00x006","57.0x00x007","57.0x00x008","57.0x00x009","57.0x00x010","57.0x00x011","57.0x00x012","57.0x00x013","57.0x02","57.0x03","57.0x04","57.0x05","57.0x06","57.0x08","57.1902","57.2100","57.4900x001","57.4901","57.4902","57.4903","57.5100","57.5100x001","57.5100x003","57.5101","57.5900x002","57.5901","57.5903","57.5906","57.6x06","57.8200","57.8900x003","57.8900x004","57.9101","57.9301","59.4x04","70.5001","70.5101","70.5400x001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合LD1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCL_DRG.LD19_group(record):
      return 'LD19'

    return 'LD1'
  else:
    return ''
