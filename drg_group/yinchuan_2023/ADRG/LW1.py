from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["N02.900x001","N02.900x002","N13.701","N23.x00","N32.803","N36.804","N39.300","N39.300x002","N39.403","N39.405","R30.000","R31.x00","R32.x00","R32.x01","R33.x00","R35.x00","R35.x00x001","R80.x00","R80.x02","R82.300","R93.403","R93.404","R93.405","R94.400","R94.402"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合LW1入组条件，匹配规则：主诊断匹配')
    
    if MDCL_DRG.LW11_group(record):
      return 'LW11'

    if MDCL_DRG.LW13_group(record):
      return 'LW13'

    if MDCL_DRG.LW15_group(record):
      return 'LW15'

    return 'LW1'
  else:
    return ''

