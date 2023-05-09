from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCX_DRG

def group(record):
  adrg_zd=["T95.300x001","Z43.100","Z43.200","Z43.201","Z43.300","Z43.301","Z43.402","Z43.403","Z43.601","Z43.603","Z45.101","Z45.201","Z45.202","Z45.804","Z45.805","Z45.806","Z46.701","Z47.800x019","Z47.800x036","Z47.900","Z48.000x001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合XT1入组条件，匹配规则：主诊断匹配')
    
    if MDCX_DRG.XT11_group(record):
      return 'XT11'

    if MDCX_DRG.XT13_group(record):
      return 'XT13'

    if MDCX_DRG.XT15_group(record):
      return 'XT15'

    return 'XT1'
  else:
    return ''

