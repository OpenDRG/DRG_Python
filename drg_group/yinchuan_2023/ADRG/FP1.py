from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I13.200x001","I21.001","I21.002","I21.003","I21.004","I21.103","I21.104","I21.106","I21.200x003","I21.200x014","I21.200x016","I21.200x017","I21.200x018","I21.200x019","I21.200x020","I21.200x021","I21.200x022","I21.200x023","I21.200x024","I21.200x025","I21.200x026","I21.200x027","I21.200x029","I21.200x030","I21.204","I21.205","I21.206","I21.207","I21.208","I21.210","I21.211","I21.212","I21.300x004","I21.303","I21.400x003","I21.401","I21.900","I22.000x001","I22.000x002","I22.100x001","I22.800x006","I22.800x007","I22.800x009","I22.800x011","I23.300x001","I50.001","I50.002","I50.101","I50.900","I50.907","R57.200"]
  adrg_zd1=[]
  adrg_ss=["39.9500x007","39.9501","39.9600x003","96.7101"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FP1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FP19_group(record):
      return 'FP19'

    return 'FP1'
  else:
    return ''

