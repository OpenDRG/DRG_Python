from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCQ_DRG

def group(record):
  adrg_zd=["D62.x00","D64.802","D64.900","D64.900x006","D64.901","D64.902","D64.903","D64.904","E80.200x004","N18.500x001+D63.8*","N18.900x012+D63.8*"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合QS4入组条件，匹配规则：主诊断匹配')
    
    if MDCQ_DRG.QS41_group(record):
      return 'QS41'

    if MDCQ_DRG.QS43_group(record):
      return 'QS43'

    if MDCQ_DRG.QS45_group(record):
      return 'QS45'

    return 'QS4'
  else:
    return ''

