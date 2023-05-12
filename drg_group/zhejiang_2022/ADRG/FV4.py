from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=["R07.101","R07.200","R07.301","R07.400","Z03.400"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and (not record.ssList or not record.ssList[0] in SS_VALID):
    message('符合FV4入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FV41_group(record):
      return 'FV41'

    if MDCF_DRG.FV43_group(record):
      return 'FV43'

    if MDCF_DRG.FV45_group(record):
      return 'FV45'

    return ''
  else:
    return ''

