from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["C79.800x863","I13.200x001","I21.300x004","I25.103","I30.100x006","I31.300","I48.000","I50.900x010","I50.900x018","I50.908","Q21.100"]
  adrg_zd1=[]
  adrg_ss=["37.0x00x002","37.0x01"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FJ1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FJ19_group(record):
      return 'FJ19'

    return 'FJ1'
  else:
    return ''

