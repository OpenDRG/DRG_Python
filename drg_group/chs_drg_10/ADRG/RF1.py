from drg_group.chs_drg_10.Base import message,intersect,SS_VALID
from drg_group.chs_drg_10.DRG import MDCR_DRG

def group(record):
  adrg_zd=["Z51.000x013","Z51.100x004","Z51.800x953","Z51.800x983"]
  adrg_zd1=[]
  adrg_ss=["54.9701","54.9702","54.9703","92.2000","92.2001","92.2100","92.2200","92.2201","92.2300","92.2301","92.2302","92.2303","92.2400","92.2400x002","92.2400x003","92.2400x004","92.2400x005","92.2400x006","92.2400x007","92.2500","92.2501","92.2601","92.2602","92.2700x002","92.2701","92.2702","92.2703","92.2704","92.2705","92.2706","92.2800","92.2900x001","92.2900x002","92.2900x003","99.2500x036","99.2500x037","99.2503","99.2504","99.2506","99.2800x006","99.2801"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss:
    message('符合RF1入组条件，匹配规则：主诊断匹配、主手术匹配')
    
    if MDCR_DRG.RF11_group(record):
      return 'RF11'

    if MDCR_DRG.RF13_group(record):
      return 'RF13'

    if MDCR_DRG.RF15_group(record):
      return 'RF15'

    return 'RF1'
  else:
    return ''

