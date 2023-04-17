from drg_group.yantai_2023.Base import message,intersect,SS_VALID
from drg_group.yantai_2023.DRG import MDCS_DRG

def group(record):
  adrg_zd=["R50.800x002","R50.801","R50.802","R50.803","R50.900","R50.900x002","R50.901"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合ST1入组条件，匹配规则：主诊断匹配')
    
    if MDCS_DRG.ST13_group(record):
      return 'ST13'

    if MDCS_DRG.ST15_group(record):
      return 'ST15'

    return 'ST1'
  else:
    return ''

