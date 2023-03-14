from drg_group.xian_2020.Base import message,intersect,SS_VALID
from drg_group.xian_2020.DRG import MDCP_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.weight and record.weight>=1500 and record.weight<2500 and record.ageDay!=None and record.ageDay<=28:
    message('符合PT1入组条件，匹配规则：体重1500至2500克、新生儿')
    
    if MDCP_DRG.PT19_group(record):
      return 'PT19'

    return 'PT1'
  else:
    return ''

