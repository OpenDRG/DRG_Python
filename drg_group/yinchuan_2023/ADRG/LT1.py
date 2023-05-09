from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["C64.x00x001","C65.x00","C66.x00","C67.000","C67.100","C67.200","C67.300","C67.400","C67.500","C67.501","C67.600","C67.700","C67.800","C67.900","C67.900x002","C68.803","C68.804","C76.303","C79.101","D09.000","D09.102","D30.000","D30.300","D30.400","D41.001","D41.101","D41.201","D41.400x001","D41.401","D41.901","Q85.900x013","Q85.903"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合LT1入组条件，匹配规则：主诊断匹配')
    
    if MDCL_DRG.LT11_group(record):
      return 'LT11'

    if MDCL_DRG.LT13_group(record):
      return 'LT13'

    if MDCL_DRG.LT15_group(record):
      return 'LT15'

    return 'LT1'
  else:
    return ''

