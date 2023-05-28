from drg_group.foshan_2022.Base import message,intersect,SS_VALID
from drg_group.foshan_2022.DRG import MDCP_DRG
from drg_group.foshan_2022.DRG_EX import PR11,PR12,PR13,PR14,PR15

def group(record):
  adrg_zd=["P22.000","P22.000x001","P22.100x003","P22.101","P22.801","P22.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ageDay!=None and record.ageDay<=28:
    message('符合PR1入组条件，匹配规则：主诊断匹配、新生儿')
    
    if PR11.group(record):
      return 'PR11'

    if PR12.group(record):
      return 'PR12'

    if PR13.group(record):
      return 'PR13'

    if PR14.group(record):
      return 'PR14'

    if PR15.group(record):
      return 'PR15'

    
    return ''
  else:
    return ''

