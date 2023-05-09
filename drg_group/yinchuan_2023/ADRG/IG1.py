from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["D21.102","M05.900","M10.002","M17.000","M17.101","M19.900","M20.501","M21.302","M24.800x052","M40.200x041","M43.006","M45.x00","M46.100","M47.101+G99.2*","M47.201","M47.801","M47.802","M48.003","M48.005","M48.901","M48.903","M50.001+G99.2*","M50.101+G55.1*","M50.201","M51.101+G55.1*","M51.103+G55.1*","M51.105+G55.1*","M51.202","M51.303","M53.101","M54.503","M65.908","M75.100","M75.400","M77.001","M77.906","M79.600x002","M80.900","M94.001","S22.000x003","S32.000x002","S51.901","S52.811","S59.700","S61.701","S61.702","S61.901","S62.611","S66.100x001","S66.100x006","S66.300x009","S68.100x001","S69.700","S79.701","S82.800x082","S83.600x002","S86.700x002","S91.301","S96.101","T84.803"]
  adrg_zd1=[]
  adrg_ss=["04.0414","04.0418","04.0426","04.2x02","04.2x04","04.2x05","04.2x06","04.3x00x017","04.3x00x024","04.3x05","04.3x10","04.3x11","04.3x12","04.3x13","04.3x18","04.4900x042","04.4912","04.7407","04.7408","04.7409","04.7410","04.7412","04.7418","04.7500x002","04.8101","04.8106"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合IG1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCI_DRG.IG13_group(record):
      return 'IG13'

    if MDCI_DRG.IG15_group(record):
      return 'IG15'

    return 'IG1'
  else:
    return ''

