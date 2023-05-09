from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["A18.002+M01.1*","A18.037+M01.1*","D16.304","M06.800x071","M06.900","M10.002","M10.903","M19.900x097","M20.100x001","M20.100x002","M20.200x001","M20.400x001","M20.501","M20.504","M21.003","M24.000","M65.908","M77.503","M84.100","M92.700x003","M92.701","Q66.600","Q66.802","Q69.900x001","Q69.900x002","Q70.400x002","Q70.900x002","S61.901","S92.300","S93.103","S93.300x031","T02.900"]
  adrg_zd1=[]
  adrg_ss=["77.5200","77.5900x001","79.7801","79.7802","79.8803","80.1801","80.4800x002","80.7800","80.8800x003","80.8800x004","80.8801","80.9800x001","81.1401","81.1700x003","81.9301","84.1102"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合ID1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCI_DRG.ID13_group(record):
      return 'ID13'

    if MDCI_DRG.ID15_group(record):
      return 'ID15'

    return 'ID1'
  else:
    return ''

