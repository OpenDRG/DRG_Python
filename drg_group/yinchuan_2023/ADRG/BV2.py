from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["D48.900x012+G73.2*","E05.900x002+G73.0*","G70.000","G70.002","G70.003","G70.004","G70.005","G70.007","G70.100","G70.202","G70.901","G70.902","G71.000","G71.000x006","G71.001","G71.100","G71.300x001","G71.301","G71.900x001","G72.301","G72.302","G72.400","G72.404","G72.800x001","G72.800x003","G72.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BV2入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BV21_group(record):
      return 'BV21'

    if MDCB_DRG.BV23_group(record):
      return 'BV23'

    if MDCB_DRG.BV25_group(record):
      return 'BV25'

    return 'BV2'
  else:
    return ''

