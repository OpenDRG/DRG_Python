from drg_group.chs_drg_10.Base import message,intersect,SS_VALID
from drg_group.chs_drg_10.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["36.1000x001","36.1000x002","36.1100","36.1200","36.1300","36.1400","36.1500","36.1600","36.1700x001","36.1900x001","36.2x00"]
  adrg_ss1=["00.6600x004","00.6601","17.5500x002","17.5500x003","17.5501","36.0400"]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss) and intersect(record.ssList,adrg_ss1):
    message('符合FC1入组条件，匹配规则：双手术匹配')
    
    if MDCF_DRG.FC19_group(record):
      return 'FC19'

    return 'FC1'
  else:
    return ''

