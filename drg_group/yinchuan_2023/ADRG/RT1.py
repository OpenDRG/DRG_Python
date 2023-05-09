from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCR_DRG

def group(record):
  adrg_zd=["C48.101","C76.300","C76.305","C76.306","C76.700","C76.700x002","C77.300x001","C77.301","C77.800","C77.900","C77.900x001","C78.604","C79.811","C79.900x001","C80.000","C80.000x001","C80.001","C80.900","C97.x00","D48.715","D48.716","D48.902","Q85.802"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合RT1入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RT11_group(record):
      return 'RT11'

    if MDCR_DRG.RT13_group(record):
      return 'RT13'

    if MDCR_DRG.RT15_group(record):
      return 'RT15'

    return 'RT1'
  else:
    return ''

