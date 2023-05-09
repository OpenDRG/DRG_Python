from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["A18.811","D24.x00","D24.x02","D48.601","I97.200","N60.000","N60.000x001","N60.101","N60.200","N60.201","N60.202","N60.300","N60.400","N60.801","N60.900","N61.x00x014","N61.x01","N61.x03","N61.x04","N61.x05","N61.x06","N61.x07","N62.x00","N62.x00x004","N62.x02","N63.x00","N63.x01","N64.100","N64.503","N64.504","Q83.100","Q83.100x001","Q83.100x002","Q85.900x009","R92.x00","T85.401"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合JV2入组条件，匹配规则：主诊断匹配')
    
    if MDCJ_DRG.JV29_group(record):
      return 'JV29'

    return 'JV2'
  else:
    return ''

