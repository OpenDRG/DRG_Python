from drg_group.taizhou_2022.Base import message,intersect,SS_VALID
from drg_group.taizhou_2022.DRG import MDCP_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["93.9000x003","93.9001","96.7101"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ageDay!=None and record.ageDay<=28:
    message('符合PK1入组条件，匹配规则：主手术匹配、新生儿')
    
    if MDCP_DRG.PK11_group(record):
      return 'PK11'

    if MDCP_DRG.PK13_group(record):
      return 'PK13'

    if MDCP_DRG.PK15_group(record):
      return 'PK15'

    return 'PK1'
  else:
    return ''

