from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["38.0400x001","38.0702","38.3401","38.4400x002","38.4500x007","38.4500x010","38.4500x011","38.4500x013","38.4500x019","38.4503","38.4504","38.4505","38.4506","38.6402","38.6701","39.2200x012","39.2303","39.5900x016","39.5900x018","39.5900x030"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FE2入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FE29_group(record):
      return 'FE29'

    return 'FE2'
  else:
    return ''

