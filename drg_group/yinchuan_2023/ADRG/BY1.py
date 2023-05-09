from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["S01.800x031","S01.800x085","S02.001","S02.002","S02.100x002","S02.100x008","S02.100x009","S02.101","S02.102","S02.113","S02.700x001","S02.701","S02.900x002","S02.902","S02.911","S06.000","S06.200x001","S06.200x011","S06.200x031","S06.200x081","S06.202","S06.204","S06.206","S06.211","S06.300x001","S06.300x011","S06.300x031","S06.300x081","S06.301","S06.302","S06.400","S06.401","S06.410","S06.500","S06.500x002","S06.500x004","S06.501","S06.502","S06.510","S06.600","S06.700x001","S06.700x002","S06.700x003","S06.700x004","S06.700x005","S06.700x006","S06.700x007","S06.710","S06.800x002","S06.800x007","S06.800x010","S06.800x011","S06.800x013","S06.801","S06.802","S06.804","S06.900","S06.910"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BY1入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BY11_group(record):
      return 'BY11'

    if MDCB_DRG.BY13_group(record):
      return 'BY13'

    if MDCB_DRG.BY15_group(record):
      return 'BY15'

    return 'BY1'
  else:
    return ''

