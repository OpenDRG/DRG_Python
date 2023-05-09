from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCP_DRG

def group(record):
  adrg_zd=["P05.001","P07.100","P07.102","P07.200x021","P07.300","P07.300x011","P07.300x021","P08.100x001","P21.000","P21.102","P22.000","P22.000x001","P22.101","P22.801","P22.900","P23.900","P24.001","P24.901","P28.500","P36.901","P39.200","P39.801","P55.101","P57.901","P59.901","P61.401","P74.802","P91.900x001","P92.500"]
  adrg_zd1=[]
  adrg_ss=["93.9000x003","93.9001","96.7101"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss) and record.ageDay!=None and record.ageDay<=28:
    message('符合PK1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配、新生儿')
    
    if MDCP_DRG.PK11_group(record):
      return 'PK11'

    if MDCP_DRG.PK13_group(record):
      return 'PK13'

    if MDCP_DRG.PK15_group(record):
      return 'PK15'

    return 'PK1'
  else:
    return ''

