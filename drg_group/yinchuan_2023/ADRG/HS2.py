from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=["K70.000","K70.100","K70.300","K70.301+I98.2*","K70.304+I98.2*","K70.306+I98.3*","K70.900","K70.901","K71.701","K72.900x003+G94.3*","K74.100","K74.300","K74.300x005+I98.2*","K74.300x006+I98.3*","K74.300x007+I98.2*","K74.300x008+I98.3*","K74.301+I98.2*","K74.302+I98.3*","K74.500","K74.600","K74.600x002","K74.600x003","K74.601","K74.602","K74.603","K74.604","K74.605","K74.606","K74.607","K74.608","K74.610","K74.613","K74.614","K74.615+I98.3*","K74.616+I98.2*","K74.617+I98.3*","K74.618+I98.3*","K74.619+I98.2*","K74.620+I98.2*","K92.801"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合HS2入组条件，匹配规则：主诊断匹配')
    
    if MDCH_DRG.HS21_group(record):
      return 'HS21'

    if MDCH_DRG.HS23_group(record):
      return 'HS23'

    if MDCH_DRG.HS25_group(record):
      return 'HS25'

    return 'HS2'
  else:
    return ''

