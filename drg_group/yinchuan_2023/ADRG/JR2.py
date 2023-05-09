from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["C43.502","C43.503","C43.504","C43.506","C43.507","C43.600x002","C43.606","C43.700x001","C43.701","C43.706","C43.707","C43.900","C44.501","C44.502","C44.503","C44.504","C44.507","C44.508","C44.509","C44.606","C44.700","C44.702","C44.703","C44.705","C44.707","C44.900","C44.901","C79.200x001","C79.200x006","C79.204","D04.500","D04.700x001","D48.500x007","L85.801"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合JR2入组条件，匹配规则：主诊断匹配')
    
    if MDCJ_DRG.JR21_group(record):
      return 'JR21'

    if MDCJ_DRG.JR23_group(record):
      return 'JR23'

    if MDCJ_DRG.JR25_group(record):
      return 'JR25'

    return 'JR2'
  else:
    return ''

