from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCK_DRG

def group(record):
  adrg_zd=["E10.500x044","E10.501+I79.2*","E10.503","E11.500x043","E11.500x044","E11.500x046","E11.500x051","E11.503","E11.504","E11.505","E11.700x031","E11.700x032","E14.500x011+I79.2*","E14.500x050","E14.500x051","E52.x00","E65.x02","E66.000","E66.801","E66.900","E66.900x001","E66.901","E67.100","E71.300","E71.308","E83.501","E83.502","E83.503","E86.x00x001","E86.x01","E87.001","E87.102","E87.201","E87.203","E87.204","E87.205","E87.303","E87.500","E87.600","E87.600x004","E87.800x004","E87.801","R29.000"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合KZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCK_DRG.KZ11_group(record):
      return 'KZ11'

    if MDCK_DRG.KZ13_group(record):
      return 'KZ13'

    if MDCK_DRG.KZ15_group(record):
      return 'KZ15'

    return 'KZ1'
  else:
    return ''

