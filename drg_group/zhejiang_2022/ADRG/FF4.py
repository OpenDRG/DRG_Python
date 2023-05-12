from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["20.7100","20.7903","38.0701","38.5701","38.8700x001","38.8701","38.8704","39.3201","44.4400x001","44.4402","55.9902","99.1000x011"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FF4入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FF41_group(record):
      return 'FF41'

    if MDCF_DRG.FF43_group(record):
      return 'FF43'

    if MDCF_DRG.FF45_group(record):
      return 'FF45'

    return ''
  else:
    return ''

