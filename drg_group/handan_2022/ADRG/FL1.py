from drg_group.handan_2022.Base import message,intersect,SS_VALID
from drg_group.handan_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I48.000","I48.100","I48.100x002","I48.100x003","I48.200","I48.300","I48.301","I48.400","I48.401","I48.900x003","I48.900x004","I48.900x015"]
  adrg_zd1=[]
  adrg_ss=["37.3402","37.3403","37.3404","37.3405","37.3406"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FL1入组条件，匹配规则：主诊断匹配、主手术匹配')
    
    if MDCF_DRG.FL19_group(record):
      return 'FL19'

    return ''
  else:
    return ''

