from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCQ_DRG

def group(record):
  adrg_zd=["D60.900x001","D61.101","D61.202","D61.300","D61.801","D61.802","D61.900","D61.900x001","D61.902","D61.903","D61.905"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合QS3入组条件，匹配规则：主诊断匹配')
    
    if MDCQ_DRG.QS31_group(record):
      return 'QS31'

    if MDCQ_DRG.QS33_group(record):
      return 'QS33'

    if MDCQ_DRG.QS35_group(record):
      return 'QS35'

    return 'QS3'
  else:
    return ''

