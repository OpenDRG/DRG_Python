from drg_group.yunnan_2022.Base import message,intersect,SS_VALID
from drg_group.yunnan_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["37.3401","37.3402","37.3403","37.3404","37.3405","37.3406"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FL2入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCF_DRG.FL29_group(record):
      return 'FL29'

    return 'FL2'
  else:
    return ''

