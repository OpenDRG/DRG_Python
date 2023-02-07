from drg_group.wuhan_2022.Base import message,intersect,SS_VALID
from drg_group.wuhan_2022.DRG import MDCP_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ageDay!=None and record.ageDay<=28:
    message('符合PC1入组条件，匹配规则：新生儿')
    
    if MDCP_DRG.PC19_group(record):
      return 'PC19'

    return 'PC1'
  else:
    return ''

