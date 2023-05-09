from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["A23.901+M49.1*","M12.500","M17.000","M17.101","M48.005","M53.207","M84.100","M84.100x031","M84.100x051","M84.100x062","M86.400","M86.910","M86.913","Q67.600","S42.300","S72.000","S82.800x082","T84.200x003","T84.600","T84.600x003","T84.604","T84.802","Z47.000x002","Z47.001"]
  adrg_zd1=[]
  adrg_ss=["78.6100x004","78.6101","78.6103","78.6105","78.6107","78.6201","78.6301","78.6303","78.6403","78.6501","78.6502","78.6600x002","78.6600x003","78.6601","78.6701","78.6702","78.6703","78.6705","78.6800x005","78.6801","78.6802","78.6803","78.6804","78.6900x002","78.6900x008","78.6900x010","78.6900x017","78.6901","78.6903","78.6905","78.6907"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合IF5入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCI_DRG.IF59_group(record):
      return 'IF59'

    return 'IF5'
  else:
    return ''

