from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["D16.800x002","D48.133","M16.000","M16.200","M16.301","M25.505","M84.100x062","Q65.000","Q65.100","Q65.801","S32.300","S32.400","S32.500x002","S32.701","S32.801","S32.802","S72.000","S72.101","S72.300","T02.300x001"]
  adrg_zd1=[]
  adrg_ss=["77.2900x001","77.2900x008","77.3904","77.6900x025","77.7901","77.8900x005","78.0900x012","78.0900x017","78.0900x022","78.0901","78.5900x027","78.5900x028","78.5900x029","78.5901","79.0902","79.1903","79.3900x025","79.3900x027","79.3900x037","79.3900x039","79.3900x043","79.3900x045","79.3900x046","79.3900x048","79.3900x050","79.3900x056","79.3900x057","81.4001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合IE1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCI_DRG.IE19_group(record):
      return 'IE19'

    return 'IE1'
  else:
    return ''

