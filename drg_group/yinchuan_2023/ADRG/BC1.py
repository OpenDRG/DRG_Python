from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["I60.000x004","I60.101","I60.200x003","I60.201","I60.300","I60.301","I60.701","I61.004","I67.100x010","I67.100x020","I67.100x021","I67.107","I67.108","I72.000x036"]
  adrg_zd1=[]
  adrg_ss=["38.6100x002","39.5100x004","39.5100x007","39.5101","39.5102","39.5103","39.5104","39.5107","39.5202"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合BC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCB_DRG.BC19_group(record):
      return 'BC19'

    return 'BC1'
  else:
    return ''

