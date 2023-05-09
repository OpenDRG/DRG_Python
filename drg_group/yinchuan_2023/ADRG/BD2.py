from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["B02.202+G53.0*","G20.x00","G20.x03","G50.000","I61.004","I61.006","I61.100x003","I61.100x013","I61.300x002","I61.902","I62.001","I62.003","S06.500x002","S06.502"]
  adrg_zd1=[]
  adrg_ss=["01.0900x007","01.2002","02.9301","02.9303","86.0900x009","86.9600x003","86.9702"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合BD2入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCB_DRG.BD29_group(record):
      return 'BD29'

    return 'BD2'
  else:
    return ''

