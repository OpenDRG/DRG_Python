from drg_group.chongqing_2022.Base import message,intersect,SS_VALID
from drg_group.chongqing_2022.DRG import MDCR_DRG

def group(record):
  adrg_zd=["Z51.000x003","Z51.000x008","Z51.000x012","Z51.001","Z51.002","Z51.003"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合RV1入组条件，匹配规则：主诊断匹配')
    
    
    if MDCR_DRG.RV11_group(record):
      return 'RV11'

    if MDCR_DRG.RV13_group(record):
      return 'RV13'

    if MDCR_DRG.RV15_group(record):
      return 'RV15'

    return ''
  else:
    return ''
