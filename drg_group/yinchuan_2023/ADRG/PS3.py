from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCP_DRG

def group(record):
  adrg_zd=["P07.300x011"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.weight and record.weight>=2000 and record.weight<2500 and record.ageDay!=None and record.ageDay<=28:
    message('符合PS3入组条件，匹配规则：主诊断匹配、体重2000至2500克、新生儿')
    
    if MDCP_DRG.PS39_group(record):
      return 'PS39'

    return 'PS3'
  else:
    return ''

