from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCP_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["96.0400","96.7101","96.7201"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ageDay!=None and record.ageDay<=28:
    message('符合PK1入组条件，匹配规则：主手术匹配、新生儿')
    
    if MDCP_DRG.PK19_group(record):
      return 'PK19'

    return ''
  else:
    return ''

