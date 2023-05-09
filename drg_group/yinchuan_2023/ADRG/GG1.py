from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCG_DRG

def group(record):
  adrg_zd=["A18.300x009+K93.0*","A18.311+K93.0*","C17.900","C18.001","C18.200","C20.x00","C79.809","D36.707","K26.501","K35.200","K35.201","K35.300","K35.301","K35.800x001","K36.x02","K40.201","K40.202","K40.900x002","K40.900x003","K43.200","K46.000x002","K56.100","K56.201","K56.500x003","K56.604","K56.700","K56.700x003","K56.701","K60.400","K63.302","K65.000","K65.003","K65.901","K66.000","K66.002","K66.006","K66.007","K91.300","K91.820","T18.900"]
  adrg_zd1=[]
  adrg_ss=["54.5100x005","54.5100x009","54.5101","54.5103","54.5900x007","54.5901","54.5903","54.5904","54.5906"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GG1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCG_DRG.GG19_group(record):
      return 'GG19'

    return 'GG1'
  else:
    return ''

