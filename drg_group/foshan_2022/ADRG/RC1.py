from drg_group.foshan_2022.Base import message,intersect,SS_VALID
from drg_group.foshan_2022.DRG import MDCR_DRG
from drg_group.foshan_2022.DRG_EX import RC11,RC12,RC14

def group(record):
  adrg_zd=["Z51.000x003","Z51.000x008","Z51.000x012","Z51.001","Z51.002","Z51.003"]
  adrg_zd1=[]
  adrg_ss=["14.2700x001","92.2000","92.2001","92.2100","92.2200","92.2201","92.2300","92.2301","92.2302","92.2303","92.2400","92.2400x002","92.2400x003","92.2400x004","92.2400x005","92.2400x006","92.2400x007","92.2500","92.2501","92.2601","92.2602","92.2700x002","92.2700x004","92.2701","92.2702","92.2703","92.2704","92.2705","92.2706","92.2800","92.2801","92.2900x001","92.2900x002","92.2900x003","92.3000","92.3001","92.3002","92.3100","92.3101","92.3102","92.3200","92.3200x001","92.3201","92.3202","92.3300","92.3900","92.4100"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合RC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if RC11.group(record):
      return 'RC11'

    if RC12.group(record):
      return 'RC12'

    if RC14.group(record):
      return 'RC14'

    
    if MDCR_DRG.RC15_group(record):
      return 'RC15'

    return ''
  else:
    return ''

