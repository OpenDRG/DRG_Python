from drg_group.yantai_2023.Base import message,intersect,SS_VALID
from drg_group.yantai_2023.DRG import MDCR_DRG

def group(record):
  adrg_zd=["Z51.000x003","Z51.000x008","Z51.000x012","Z51.001","Z51.002","Z51.003","Z51.806","Z51.811"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合RV1入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RV11_group(record):
      return 'RV11'

    if MDCR_DRG.RV15_group(record):
      return 'RV15'

    return 'RV1'
  else:
    return ''

