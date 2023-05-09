from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I20.000","I20.801","I21.001","I21.003","I21.004","I21.103","I21.106","I21.200x014","I21.200x018","I21.200x019","I21.200x021","I21.200x023","I21.200x025","I21.200x026","I21.200x030","I21.204","I21.207","I21.208","I21.210","I21.211","I21.212","I21.300x004","I21.401","I21.900","I24.901","I25.103","I25.500","I50.900x018"]
  adrg_zd1=[]
  adrg_ss=["36.0601","36.0700x004","36.0701"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FM1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FM19_group(record):
      return 'FM19'

    return 'FM1'
  else:
    return ''

