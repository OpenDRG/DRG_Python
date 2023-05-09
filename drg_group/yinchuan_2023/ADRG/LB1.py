from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["N13.000","N13.201","N13.202","N13.203","N13.501","N13.601","N13.602","N13.603","N18.300","N20.000","N20.000x001","N20.100","N20.200x001","N21.000","N28.810","N28.833"]
  adrg_zd1=[]
  adrg_ss=["55.0300x003","55.0302","55.0400x005","55.0400x006","55.0400x007","55.0400x009","55.0400x010","55.0401","55.0402","55.0403","55.0404","55.1105"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合LB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCL_DRG.LB19_group(record):
      return 'LB19'

    return 'LB1'
  else:
    return ''

