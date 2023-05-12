from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.5000x001","00.5001","00.5002","00.5301","17.5100","17.5200","37.8000x001","37.8001","37.8101","37.8201","37.8300x002","37.8301"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FK1入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FK11_group(record):
      return 'FK11'

    if MDCF_DRG.FK13_group(record):
      return 'FK13'

    if MDCF_DRG.FK15_group(record):
      return 'FK15'

    return ''
  else:
    return ''

