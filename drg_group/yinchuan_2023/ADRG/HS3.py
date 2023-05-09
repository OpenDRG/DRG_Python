from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=["B15.900","B15.901","B15.902","B16.901","B16.904","B16.905","B17.000","B17.200","B17.202","B17.900","B17.900x002","B17.900x004","B17.902","B18.000","B18.003","B18.004","B18.100","B18.104","B18.105","B18.106","B18.107","B18.200","B18.201","B18.204","B18.900","B18.902","B18.903","B19.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合HS3入组条件，匹配规则：主诊断匹配')
    
    if MDCH_DRG.HS31_group(record):
      return 'HS31'

    if MDCH_DRG.HS33_group(record):
      return 'HS33'

    if MDCH_DRG.HS35_group(record):
      return 'HS35'

    return 'HS3'
  else:
    return ''

