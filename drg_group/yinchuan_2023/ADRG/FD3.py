from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["I33.000x004","Q21.000","Q21.100","Q21.101","Q21.102","Q24.503","Q25.000","Q25.403","T82.503"]
  adrg_zd1=[]
  adrg_ss=["35.5200x001","35.5200x002","35.5201","35.5500x001","36.9900x005","39.7800x008","39.7900x402"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FD3入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FD39_group(record):
      return 'FD39'

    return 'FD3'
  else:
    return ''

