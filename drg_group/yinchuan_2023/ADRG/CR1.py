from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCC_DRG

def group(record):
  adrg_zd=["C44.100x002","C44.100x003","C69.200","C69.600","C69.900","C79.405","C79.409"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合CR1入组条件，匹配规则：主诊断匹配')
    
    if MDCC_DRG.CR19_group(record):
      return 'CR19'

    return 'CR1'
  else:
    return ''

