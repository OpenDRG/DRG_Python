from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCS_DRG

def group(record):
  adrg_zd=["A02.100","A32.700","A40.300","A40.800","A40.900","A41.000","A41.100x002","A41.101","A41.200","A41.400","A41.500x083","A41.501","A41.503","A41.504","A41.506","A41.804","A41.805","A41.807","A41.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合SR1入组条件，匹配规则：主诊断匹配')
    
    if MDCS_DRG.SR11_group(record):
      return 'SR11'

    if MDCS_DRG.SR13_group(record):
      return 'SR13'

    if MDCS_DRG.SR15_group(record):
      return 'SR15'

    return 'SR1'
  else:
    return ''

