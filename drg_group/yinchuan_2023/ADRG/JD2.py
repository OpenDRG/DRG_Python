from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCJ_DRG

def group(record):
  adrg_zd=["L03.107","L08.900","L08.903","L08.904","L08.910","L89.200","T01.301","T11.101","T14.001","T14.101"]
  adrg_zd1=[]
  adrg_ss=["86.2800x012"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合JD2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCJ_DRG.JD29_group(record):
      return 'JD29'

    return 'JD2'
  else:
    return ''

