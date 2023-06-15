from drg_group.yunnan_2022.Base import message,intersect,SS_VALID
from drg_group.yunnan_2022.DRG import MDCB_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["99.1000","99.1005","99.1006","99.1008","99.1009"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合BL1入组条件，匹配规则：主手术匹配')
    
    
    if MDCB_DRG.BL19_group(record):
      return 'BL19'

    return ''
  else:
    return ''
