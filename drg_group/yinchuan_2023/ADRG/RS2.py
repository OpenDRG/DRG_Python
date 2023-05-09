from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCR_DRG

def group(record):
  adrg_zd=["C90.000","C90.000x005","C90.000x021","C90.000x022","C90.000x024","C90.000x028","C90.000x033","C90.000x034","C90.000x036","C90.000x037","C90.000x038","C90.000x040","C90.001","C90.200x008","C90.302","C90.303","D89.801"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合RS2入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RS21_group(record):
      return 'RS21'

    if MDCR_DRG.RS23_group(record):
      return 'RS23'

    if MDCR_DRG.RS25_group(record):
      return 'RS25'

    return 'RS2'
  else:
    return ''

