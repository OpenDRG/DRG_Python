from drg_group.suzhou_2022.Base import message,intersect,SS_VALID
from drg_group.suzhou_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["36.0601","36.0602","36.0700x004","36.0701"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FM1入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FM19_group(record):
      return 'FM19'

  return ''

