from drg_group.yancheng_2023.Base import message,intersect,SS_VALID
from drg_group.yancheng_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=["E10.400x311+G99.0*","I95.100","I95.101","R55.x00x001","R55.x00x002","R55.x00x003","R55.x00x004","R55.x00x005","R55.x00x006","R55.x00x007","R55.x00x008","R55.x00x009","R55.x00x010","R55.x00x011","R55.x00x012","R55.x00x013","R55.x00x014","R55.x02"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合FV3入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FV33_group(record):
      return 'FV33'

    if MDCF_DRG.FV35_group(record):
      return 'FV35'

    return 'FV3'
  else:
    return ''

