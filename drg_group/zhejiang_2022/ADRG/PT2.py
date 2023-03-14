from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCP_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.weight and record.weight>=2500 and record.ageDay!=None and record.ageDay<=28:
    message('符合PT2入组条件，匹配规则：体重大于2500克、新生儿')
    
    if MDCP_DRG.PT21_group(record):
      return 'PT21'

    if MDCP_DRG.PT23_group(record):
      return 'PT23'

    if MDCP_DRG.PT25_group(record):
      return 'PT25'

    return 'PT2'
  else:
    return ''

