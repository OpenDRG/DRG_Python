from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCW_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True:
    message('符合WJ1入组条件，匹配规则：')
    
    if MDCW_DRG.WJ19_group(record):
      return 'WJ19'

    return 'WJ1'
  else:
    return ''

