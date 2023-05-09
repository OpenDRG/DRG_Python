from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["N10.x02","N11.802","N11.900x001","N12.x02","N13.600","N13.601","N13.602","N13.603","N13.605","N15.101","N15.102","N15.900x002","N15.901","N28.834","N28.839","N30.000","N30.201","N30.801","N34.001","N34.101","N34.204","N34.300","N39.000","N39.001","T83.500x003"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合LU1入组条件，匹配规则：主诊断匹配')
    
    if MDCL_DRG.LU11_group(record):
      return 'LU11'

    if MDCL_DRG.LU13_group(record):
      return 'LU13'

    if MDCL_DRG.LU15_group(record):
      return 'LU15'

    return 'LU1'
  else:
    return ''

