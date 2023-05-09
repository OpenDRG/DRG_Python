from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["G40.000","G40.001","G40.004","G40.100","G40.100x001","G40.100x004","G40.100x006","G40.100x007","G40.100x010","G40.100x011","G40.103","G40.200","G40.200x001","G40.200x002","G40.200x003","G40.200x004","G40.200x006","G40.200x013","G40.300","G40.300x003","G40.300x006","G40.300x007","G40.300x008","G40.300x010","G40.300x013","G40.300x017","G40.300x018","G40.300x019","G40.300x023","G40.302","G40.307","G40.308","G40.309","G40.310","G40.400x001","G40.400x002","G40.403","G40.404","G40.505","G40.600","G40.700","G40.800x004","G40.805","G40.900","G40.900x005","G41.000","G41.000x002","G41.000x003","G41.001","G41.101","G41.200x004","G41.802","G41.806","G41.900","R56.800x001","R56.800x003","R56.800x005","R56.801","R56.803","T90.503"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BV1入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BV11_group(record):
      return 'BV11'

    if MDCB_DRG.BV13_group(record):
      return 'BV13'

    if MDCB_DRG.BV15_group(record):
      return 'BV15'

    return 'BV1'
  else:
    return ''

