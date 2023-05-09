from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCQ_DRG

def group(record):
  adrg_zd=["D56.800","D56.900","D58.000","D58.205","D58.206","D58.901","D59.101","D59.103","D59.500x001","D59.501","D59.602","D59.901","D59.902"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合QS2入组条件，匹配规则：主诊断匹配')
    
    if MDCQ_DRG.QS23_group(record):
      return 'QS23'

    if MDCQ_DRG.QS25_group(record):
      return 'QS25'

    return 'QS2'
  else:
    return ''

