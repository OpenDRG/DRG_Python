from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I20.000","I20.801","I21.001","I21.004","I21.103","I21.211","I21.300x004","I21.302","I21.401","I21.900","I24.002","I25.100x003","I25.103","I25.300x008","I25.901","I35.100","I77.110"]
  adrg_zd1=[]
  adrg_ss=["36.0300x002","36.0301","36.1000x001","36.1100","36.1200","36.1300","36.1400","36.1500","36.9900x002","36.9900x006"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FC1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FC19_group(record):
      return 'FC19'

    return 'FC1'
  else:
    return ''

