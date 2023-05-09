from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCR_DRG

def group(record):
  adrg_zd=["C81.100","C81.900","C82.000","C82.100","C82.200","C82.900","C83.000","C83.003","C83.300","C83.300x006","C83.700","C83.800x008","C83.900","C84.000x002","C84.400","C84.404","C84.502","C84.600","C85.100","C85.100x010","C85.707","C85.900","C85.900x006","C85.900x010","C85.900x015","C85.900x023","C85.900x025","C85.900x031","C85.900x040","C86.000","C88.000","C88.401","C91.100","C92.100x001","C92.100x016","C92.706","C93.900","C94.703","C95.900","C96.604","D45.x00","D46.200","D46.500","D46.600","D46.700x001","D46.700x003","D46.700x006","D46.700x007","D46.900","D46.900x002","D46.900x006","D47.100","D47.100x004","D47.100x008","D47.200","D47.300","D47.401","D47.402","D47.700x006","D47.700x007","D47.900x001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合RS1入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RS11_group(record):
      return 'RS11'

    if MDCR_DRG.RS13_group(record):
      return 'RS13'

    if MDCR_DRG.RS15_group(record):
      return 'RS15'

    return 'RS1'
  else:
    return ''

