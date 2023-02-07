from drg_group.beijing_2022.Base import message,intersect,SS_VALID
from drg_group.beijing_2022.DRG import MDCR_DRG

def group(record):
  adrg_zd=["D19.900x001","D36.700x011","D36.700x012","D36.700x021","D36.700x023","D36.700x025","D36.700x028","D36.704","D36.705","D36.709","D36.710","D36.711"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合RT2入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RT29_group(record):
      return 'RT29'

    return 'RT2'
  else:
    return ''

