from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["N13.000","N13.100x001","N13.204","N13.300x005","N13.301","N13.400","N13.501","N13.503","N13.506","N20.000","N20.001","N32.000","N35.000","N35.800","N35.901","N99.101","Q62.101","Q62.103"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合LX1入组条件，匹配规则：主诊断匹配')
    
    if MDCL_DRG.LX19_group(record):
      return 'LX19'

    return 'LX1'
  else:
    return ''

