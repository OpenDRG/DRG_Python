from drg_group.foshan_2022.Base import message,intersect,SS_VALID
from drg_group.foshan_2022.DRG import MDCP_DRG
from drg_group.foshan_2022.DRG_EX import PK11,PK12,PK13,PK14,PK15

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["93.9000x003","93.9001","96.7101"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss) and record.ageDay!=None and record.ageDay<=28:
    message('符合PK1入组条件，匹配规则：主手术匹配、某一手术匹配、新生儿')
    
    if PK11.group(record):
      return 'PK11'

    if PK12.group(record):
      return 'PK12'

    if PK13.group(record):
      return 'PK13'

    if PK14.group(record):
      return 'PK14'

    if PK15.group(record):
      return 'PK15'

    
    if MDCP_DRG.PK10_group(record):
      return 'PK10'

    return ''
  else:
    return ''

