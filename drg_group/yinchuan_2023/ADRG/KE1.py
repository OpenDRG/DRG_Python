from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCK_DRG

def group(record):
  adrg_zd=["E16.803","E66.000"]
  adrg_zd1=[]
  adrg_ss=["43.7x03","43.8201","43.8903"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合KE1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCK_DRG.KE19_group(record):
      return 'KE19'

    return 'KE1'
  else:
    return ''

