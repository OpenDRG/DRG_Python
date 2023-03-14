from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCS_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True:
    message('符合SB1入组条件，匹配规则：')
    
    if MDCS_DRG.SB19_group(record):
      return 'SB19'

    return 'SB1'
  else:
    return ''

