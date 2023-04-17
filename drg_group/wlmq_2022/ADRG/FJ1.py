from drg_group.wlmq_2022.Base import message,intersect,SS_VALID
from drg_group.wlmq_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.6700x001","00.6701","37.0x00x002","37.0x01","37.2400","37.2401","37.2501","37.7901","37.7902"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FJ1入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FJ19_group(record):
      return 'FJ19'

    return 'FJ1'
  else:
    return ''

