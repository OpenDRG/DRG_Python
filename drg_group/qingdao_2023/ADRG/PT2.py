from drg_group.qingdao_2023.Base import message,intersect,SS_VALID
from drg_group.qingdao_2023.DRG import MDCP_DRG

def group(record):
  adrg_zd=["P07.200x011","P07.300x021"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and intersect(record.zdList,adrg_zd) and record.weight and record.weight>=2500 and record.ageDay!=None and record.ageDay<=28:
    message('符合PT2入组条件，匹配规则：某一诊断匹配、体重大于2500克、新生儿')
    
    return 'PT2'
  else:
    return ''

