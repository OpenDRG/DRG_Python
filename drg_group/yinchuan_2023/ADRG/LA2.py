from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["C64.x00x001","C67.000","C67.100","C67.200","C67.300","C67.400","C67.500","C67.800","C67.900","C67.900x002","C79.101","D41.400x001"]
  adrg_zd1=[]
  adrg_ss=["57.4900x001","57.4901","57.4903","57.4904","57.5900x002","57.5901","57.5902","57.5906","57.6x00","57.6x04","57.6x06","57.7100","57.7103","57.7900x001","57.7901","57.8700x005","57.8701"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合LA2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCL_DRG.LA29_group(record):
      return 'LA29'

    return 'LA2'
  else:
    return ''

