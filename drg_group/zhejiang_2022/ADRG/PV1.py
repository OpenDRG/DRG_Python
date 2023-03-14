from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCP_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True:
    message('符合PV1入组条件，匹配规则：')
    
    if MDCP_DRG.PV11_group(record):
      return 'PV11'

    if MDCP_DRG.PV13_group(record):
      return 'PV13'

    if MDCP_DRG.PV15_group(record):
      return 'PV15'

    return 'PV1'
  else:
    return ''

