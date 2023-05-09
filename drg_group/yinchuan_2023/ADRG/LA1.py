from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCL_DRG

def group(record):
  adrg_zd=["C64.x00x001","C65.x00","C68.801","C68.805","D30.000","D41.001","D41.101","Q85.903"]
  adrg_zd1=[]
  adrg_ss=["40.5911","55.4x00","55.4x02","55.4x03","55.4x04","55.5101","55.5103","55.5104"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合LA1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCL_DRG.LA19_group(record):
      return 'LA19'

    return 'LA1'
  else:
    return ''

