from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCS_DRG

def group(record):
  adrg_zd=["T85.703","T85.711","T85.712","T98.200x012","T98.200x021"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合SS1入组条件，匹配规则：主诊断匹配')
    
    if MDCS_DRG.SS11_group(record):
      return 'SS11'

    return 'SS1'
  else:
    return ''

