from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["A80.400x001","A83.000x001","A83.000x002","A83.000x003","A83.000x004","A83.000x005","A85.800","A86.x00","A86.x01","A86.x02","A87.800","A87.900","A87.901","B00.300+G02.0*","B00.400+G05.1*","G04.001","G04.800x005","G04.909"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BT1入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BT11_group(record):
      return 'BT11'

    if MDCB_DRG.BT13_group(record):
      return 'BT13'

    if MDCB_DRG.BT15_group(record):
      return 'BT15'

    return 'BT1'
  else:
    return ''

