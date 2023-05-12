from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["36.1000x001","36.1000x002","36.1100","36.1200","36.1300","36.1400","36.1500","36.1600","36.1700x001","36.1900x001","36.2x00"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FC3入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FC31_group(record):
      return 'FC31'

    if MDCF_DRG.FC33_group(record):
      return 'FC33'

    if MDCF_DRG.FC35_group(record):
      return 'FC35'

    return ''
  else:
    return ''

