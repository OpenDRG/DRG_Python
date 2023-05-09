from drg_group.linfen_2022.Base import message,intersect,SS_VALID
from drg_group.linfen_2022.DRG import MDCU_DRG

def group(record):
  adrg_zd=["F10.000","F10.001","F10.002","F10.003","F10.100","F10.100x002","F10.200","F10.201","F10.300","F10.400","F10.401","F10.500","F10.501","F10.502","F10.503","F10.504","F10.505","F10.600","F10.600x002","F10.601","F10.700","F10.700x091","F10.701","F10.800","F10.900","R78.000","T51.001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合UR1入组条件，匹配规则：主诊断匹配')
    
    if MDCU_DRG.UR19_group(record):
      return 'UR19'

    return 'UR1'
  else:
    return ''

