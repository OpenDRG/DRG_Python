from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCT_DRG

def group(record):
  adrg_zd=["F72.000x001","F78.900","F79.000","F79.000x001","F79.100","F79.800","F79.900","F80.000","F80.100","F80.900","F81.900","F82.x00","F83.x00","F84.000","F84.000x001","F84.001","F84.800","F84.900x001","F90.000x001","F93.900","F95.800","F98.000","F98.001","Q90.900","Q93.501"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合TU1入组条件，匹配规则：主诊断匹配')
    
    if MDCT_DRG.TU19_group(record):
      return 'TU19'

    return 'TU1'
  else:
    return ''

