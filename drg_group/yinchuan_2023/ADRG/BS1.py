from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["E16.107+G94.8*","G93.500x001","G93.500x005","G93.500x007","G93.501","R40.100x003","R40.200","R40.200x002","R40.200x004","R40.201"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BS1入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BS11_group(record):
      return 'BS11'

    if MDCB_DRG.BS13_group(record):
      return 'BS13'

    if MDCB_DRG.BS15_group(record):
      return 'BS15'

    return 'BS1'
  else:
    return ''

