from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["I12.000x001","I13.100x001","N00.301","N00.802","N00.900","N00.900x002","N00.901","N00.902","N01.700x001","N17.000","N17.001","N17.002","N17.800","N17.900","N17.900x002","N17.900x003","N17.900x004","N18.300","N18.400","N18.500","N18.501","N18.902","N18.904","N19.x00","N19.x01","N19.x03","T79.500","T86.100x003","T86.102","T86.106"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合LR1入组条件，匹配规则：主诊断匹配')
    
    if MDCL_DRG.LR11_group(record):
      return 'LR11'

    if MDCL_DRG.LR13_group(record):
      return 'LR13'

    if MDCL_DRG.LR15_group(record):
      return 'LR15'

    return 'LR1'
  else:
    return ''

