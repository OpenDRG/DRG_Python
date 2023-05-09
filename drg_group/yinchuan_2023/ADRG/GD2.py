from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCG_DRG

def group(record):
  adrg_zd=["C18.100","C78.503","D12.100","D37.300x001","K35.200","K35.201","K35.300","K35.301","K35.800x001","K36.x00x003","K36.x02","K37.x00","K37.x00x002","K38.801","K40.201","K40.903","K56.700","K57.000","K57.102","K65.000","K65.003","K65.901","Q40.200x010","T18.801"]
  adrg_zd1=[]
  adrg_ss=["47.0100","47.0901","47.1100","47.2x00","47.2x01"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GD2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCG_DRG.GD21_group(record):
      return 'GD21'

    if MDCG_DRG.GD23_group(record):
      return 'GD23'

    if MDCG_DRG.GD25_group(record):
      return 'GD25'

    return 'GD2'
  else:
    return ''

