from drg_group.lanzhou_2023.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2023.DRG import MDCR_DRG

def group(record):
  adrg_zd=["Z08.000","Z08.100","Z08.200","Z08.700","Z08.800x001","Z08.800x002","Z08.800x003","Z08.800x004","Z08.900","Z09.100","Z09.200","Z54.001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合RW1入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RW11_group(record):
      return 'RW11'

    if MDCR_DRG.RW1B_group(record):
      return 'RW14'

    return 'RW1'
  else:
    return ''

