from drg_group.wuhan_2022.Base import message,intersect,SS_VALID
from drg_group.wuhan_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=["R07.101","R07.200","R07.301","R07.400","Z03.400"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合FV4入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FV49_group(record):
      return 'FV49'

    return 'FV4'
  else:
    return ''

