from drg_group.linfen_2022.Base import message,intersect,SS_VALID
from drg_group.linfen_2022.DRG import MDCE_DRG

def group(record):
  adrg_zd=["B06.800","B37.100","B37.101+J17.2*","B37.800x083","B37.803","B38.000","B38.000x001+J17.2*","B38.100","B38.100x001+J17.2*","B38.200","B38.200x001+J17.2*","B39.000","B39.000x001+J17.2*","B39.100","B39.100x001+J17.2*","B39.200","B39.200x001+J17.2*","B40.000","B40.100","B40.200","B41.000","B42.000+J99.8*","B44.000x001+J99.8*","B44.101+J99.8*","B44.102+J17.2*","B45.000","B45.000x002+J99.8*","B46.000x001+J99.8*","B48.500+J17.2*","B48.501+J17.2*","B48.502+J17.2*","B49.x00x011","B49.x13","B49.x14+J99.8*"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合ES2入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.ES29_group(record):
      return 'ES29'

    return 'ES2'
  else:
    return ''

