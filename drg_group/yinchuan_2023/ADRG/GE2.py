from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCG_DRG

def group(record):
  adrg_zd=["K40.900x003","K44.900x001","K44.901","K45.002","K45.807"]
  adrg_zd1=[]
  adrg_ss=["53.7101","53.7201","53.7202","53.9x02","53.9x03","53.9x05"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GE2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCG_DRG.GE29_group(record):
      return 'GE29'

    return 'GE2'
  else:
    return ''

