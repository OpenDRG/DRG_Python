from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=["C22.900","K70.304+I98.2*","K70.305+I98.3*","K70.306+I98.3*","K74.100","K74.300","K74.300x006+I98.3*","K74.300x008+I98.3*","K74.301+I98.2*","K74.602","K74.603","K74.607","K74.615+I98.3*","K74.617+I98.3*","K74.618+I98.3*","K74.619+I98.2*","K74.620+I98.2*"]
  adrg_zd1=[]
  adrg_ss=["43.4100x020","96.0601"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合HK1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCH_DRG.HK19_group(record):
      return 'HK19'

    return 'HK1'
  else:
    return ''

