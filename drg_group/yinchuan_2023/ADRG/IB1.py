from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["A23.901+M49.1*","M41.900","M41.900x061","M41.901","M43.006","M47.101+G99.2*","M48.002","M48.003","M48.005","M51.101+G55.1*","M51.202","M53.203","M53.207","M80.801","S22.000x051"]
  adrg_zd1=[]
  adrg_ss=["03.0900x007","03.0900x023","78.0900x008","78.0900x009","80.5100x008","80.5100x025","80.5101","80.5104","80.5105","81.0200x001","81.0300x001","81.0500x006","81.0501","81.0502","81.0600x005","81.0601","81.0701","81.0702","81.0800x016","81.0800x018","81.0801","81.0802","81.3500x003","81.3600x003","81.3800x003","81.6300","81.6400x003"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合IB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCI_DRG.IB19_group(record):
      return 'IB19'

    return 'IB1'
  else:
    return ''

