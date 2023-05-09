from drg_group.yunnan_2022.Base import message,intersect,SS_VALID
from drg_group.yunnan_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.6700x001","00.6701","36.0901","37.0x00x002","37.0x01","37.2400","37.2401","37.2501","37.7901","37.7902","37.9300x001","38.0500x002","38.7x01","38.7x02","38.8401","38.8501","38.8502","40.2900x002","40.2900x008"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FJ1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FJ11_group(record):
      return 'FJ11'

    if MDCF_DRG.FJ15_group(record):
      return 'FJ15'

    return 'FJ1'
  else:
    return ''

