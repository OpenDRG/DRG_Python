from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCO_DRG

def group(record):
  adrg_zd=["O75.700x001","O80.000","O80.100","O80.800","O80.900","O84.000","Z38.000x001","Z38.100x001","Z38.200x001","Z38.300x001","Z38.400x001","Z38.500x001","Z38.600x001","Z38.700x001","Z38.800x001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and (not record.ssList or not record.ssList[0] in SS_VALID):
    message('符合OR1入组条件，匹配规则：主诊断匹配')
    
    if MDCO_DRG.OR11_group(record):
      return 'OR11'

    if MDCO_DRG.OR13_group(record):
      return 'OR13'

    if MDCO_DRG.OR15_group(record):
      return 'OR15'

    if MDCO_DRG.OR19_group(record):
      return 'OR19'

    return ''
  else:
    return ''

