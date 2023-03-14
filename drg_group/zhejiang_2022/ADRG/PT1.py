from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCP_DRG

def group(record):
  adrg_zd=["P05.001","P05.102","P07.100","P07.101","P07.200","P07.200x011","P07.200x021","P07.300","P07.300x001","P07.300x011","P07.300x021"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd and record.weight and record.weight>=1500 and record.weight<2500 and record.ageDay!=None and record.ageDay<=28:
    message('符合PT1入组条件，匹配规则：主诊断匹配、体重1500至2500克、新生儿')
    
    if MDCP_DRG.PT11_group(record):
      return 'PT11'

    if MDCP_DRG.PT13_group(record):
      return 'PT13'

    if MDCP_DRG.PT15_group(record):
      return 'PT15'

    return 'PT1'
  else:
    return ''

