from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCC_DRG

def group(record):
  adrg_zd=["E11.302+H28.0*","E14.300x061+H28.0*","E88.906+H28.1*","H25.000","H25.000x003","H25.000x006","H25.001","H25.002","H25.004","H25.100","H25.800","H25.900","H26.000x001","H26.100","H26.200","H26.202","H26.300","H26.400","H26.801","H26.802","H26.900","H27.000","H27.100","H27.101","Q12.000"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合CW1入组条件，匹配规则：主诊断匹配')
    
    if MDCC_DRG.CW19_group(record):
      return 'CW19'

    return 'CW1'
  else:
    return ''

