from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCP_DRG

def group(record):
  adrg_zd=["P59.901","P76.900","P77.x01","P78.000x003","P78.100x001","P78.800x007"]
  adrg_zd1=[]
  adrg_ss=["45.6201","45.6205","45.6207","46.3904","47.0100","47.0901","53.0202","54.1100","54.1903","54.5100x009","54.5904","54.6101"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss) and record.ageDay!=None and record.ageDay<=28:
    message('符合PC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配、新生儿')
    
    if MDCP_DRG.PC11_group(record):
      return 'PC11'

    if MDCP_DRG.PC13_group(record):
      return 'PC13'

    return 'PC1'
  else:
    return ''

