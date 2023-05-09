from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCQ_DRG

def group(record):
  adrg_zd=["D48.906+D63.0*","D50.000","D50.001","D50.801","D50.900","D50.901","D51.001","D51.101","D52.000x001","D52.001","D53.100","D53.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合QS1入组条件，匹配规则：主诊断匹配')
    
    if MDCQ_DRG.QS11_group(record):
      return 'QS11'

    if MDCQ_DRG.QS13_group(record):
      return 'QS13'

    if MDCQ_DRG.QS15_group(record):
      return 'QS15'

    return 'QS1'
  else:
    return ''

