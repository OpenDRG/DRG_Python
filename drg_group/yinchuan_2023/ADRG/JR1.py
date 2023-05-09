from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["C50.000x001","C50.001","C50.100","C50.200","C50.300","C50.400","C50.500","C50.800x005","C50.801","C50.802","C50.803","C50.804","C50.900","C50.900x005","C50.901","C79.800x831","D05.000","D05.100","D05.900","D48.600x001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合JR1入组条件，匹配规则：主诊断匹配')
    
    if MDCJ_DRG.JR19_group(record):
      return 'JR19'

    return 'JR1'
  else:
    return ''

