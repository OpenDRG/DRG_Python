from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCT_DRG

def group(record):
  adrg_zd=["F43.000","F44.401","F44.402","F44.404","F44.501","F44.601","F44.800x002","F44.802","F44.805","F44.900","F44.902","F44.903","F45.000","F45.300","F45.302","F45.304","F45.306","F45.308","F45.310","F45.403","F45.801","F45.803","F45.804","F45.805","F45.806","F45.900","F48.000","F48.001","F48.802","F48.901","F95.201","F95.900"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合TS2入组条件，匹配规则：主诊断匹配')
    
    if MDCT_DRG.TS29_group(record):
      return 'TS29'

    return 'TS2'
  else:
    return ''

