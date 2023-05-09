from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["B00.000","L20.802","L20.900","L21.900","L23.300","L23.900","L23.901","L24.400","L25.000","L25.100","L25.201","L25.300","L25.800","L25.900","L27.003","L27.004","L27.005","L27.101","L27.200","L28.000","L28.001","L28.002","L28.100","L28.200","L28.203","L29.000","L29.800","L29.802","L29.900","L30.000","L30.100","L30.202","L30.300","L30.301","L30.400x004","L30.500","L30.800","L30.802","L30.900","L30.901","L30.902","L30.903","L30.904","L30.905","L41.900","L56.200","L57.801","L57.802","L58.900","L59.000","L81.701"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合JS2入组条件，匹配规则：主诊断匹配')
    
    if MDCJ_DRG.JS29_group(record):
      return 'JS29'

    return 'JS2'
  else:
    return ''

