from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCQ_DRG

def group(record):
  adrg_zd=["D46.000","D46.000x002","D46.000x003","D46.001","D46.100","D46.100x002","D46.100x012","D46.200","D46.201x001","D46.203","D46.400","D46.500","D46.600","D62.x00","D64.000","D64.001","D64.100","D64.200","D64.300","D64.300x002","D64.400x001","D64.401","D64.800x002","D64.801","D64.802","D64.803","D64.900","D64.900x005","D64.900x006","D64.900x007","D64.901","D64.902","D64.903","D64.904","N18.500x001+D63.8*"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and (not record.ssList or not record.ssList[0] in SS_VALID):
    message('符合QS4入组条件，匹配规则：主诊断匹配')
    
    if MDCQ_DRG.QS41_group(record):
      return 'QS41'

    if MDCQ_DRG.QS43_group(record):
      return 'QS43'

    if MDCQ_DRG.QS45_group(record):
      return 'QS45'

    return ''
  else:
    return ''

